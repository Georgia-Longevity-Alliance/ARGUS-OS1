//! argus-agent V1.1 — agent loop (P1) + modes (P4) + P3 (rewriter, reflection behind flags).
//! Tools: file.read, file.write, shell, memory.set, memory.note, memory.recall, memory.lesson.
use crate::memory::{Memory, NoteKind};
use serde::{Deserialize, Serialize};

/// Modes (P4): default / plan / auto / bypass. Mode is session state, not config.
#[derive(Deserialize, Debug, Clone, Copy, PartialEq, Eq, Default)]
#[serde(rename_all = "lowercase")]
pub enum Mode {
    #[default]
    Default,
    Plan,
    Auto,
    Bypass,
}

#[derive(Deserialize, Debug)]
pub struct ToolCall {
    pub tool: String,
    #[serde(default)]
    pub args: serde_json::Value,
    #[serde(default)]
    pub dangerous: bool,
}

#[derive(Debug)]
pub struct ToolResult {
    pub tool: String,
    pub ok: bool,
    pub summary: String,
}

/// One-step model decision.
pub enum AgentDecision {
    Tools(Vec<ToolCall>),
    Reply(String),
}

/// One reflection item (P3B): SET fact or NOTE note.
pub enum ReflectionItem {
    Set {
        key: String,
        value: String,
        pinned: bool,
        keywords: Vec<String>,
    },
    Note {
        content: String,
        tags: Vec<String>,
        kind: NoteKind,
    },
}

pub trait Model {
    fn decide(&self, prompt: &str) -> AgentDecision;
    fn compress(&self, results: &[ToolResult]) -> String;
    /// P3B: extract durable facts/notes from a transcript window (reflection).
    fn reflect(&self, window: &str) -> Vec<ReflectionItem>;
    /// V3.0: LLM distillation of a procedure from a cluster of repeated notes.
    fn distill_procedure(&self, tag: &str, notes: &str) -> Option<(String, Vec<String>)>;
    /// V3.1: LLM distillation of a lesson (activation + principle) from a cluster.
    fn distill_lesson(&self, tag: &str, notes: &str) -> Option<(String, String)>;
}

/// Loop config (P1) + P3 flags.
#[derive(Debug, Clone)]
pub struct LoopConfig {
    pub max_steps: u64,
    pub max_duration_min: u64,
    // P3A: rewriter for short referential queries
    pub rewriter: bool,
    // P3B: sliding-window reflection
    pub reflection: bool,
    pub reflection_every: u64,
    pub reflection_window: u64,
}

impl Default for LoopConfig {
    fn default() -> Self {
        LoopConfig {
            max_steps: 1000,
            max_duration_min: 120,
            rewriter: true,
            reflection: true,
            reflection_every: 3,
            reflection_window: 5,
        }
    }
}

pub struct AgentLoop<'a> {
    pub model: &'a dyn Model,
    pub mode: Mode,
    pub cfg: LoopConfig,
    pub approve: bool,
    pub cwd: String,
    pub last_transcript: Vec<String>,
    pub goal: String,
    /// installed skills (V1.5) — indexed into the prompt, body via skill.view
    pub skills: Vec<crate::skills::Skill>,
    /// V2.0: initial session transcript (for --session continuation)
    pub seed: Vec<String>,
    /// V2.3: plugin hooks (before_step/after_step/on_done)
    pub plugins: Vec<crate::plugins::Plugin>,
}

impl<'a> AgentLoop<'a> {
    pub fn run(&mut self, goal: &str, mem: &mut Memory) -> String {
        self.goal = goal.to_string();
        let started = std::time::Instant::now();
        let mut step: u64 = 0;
        let mut transcript: Vec<String> = self.seed.clone();
        self.last_transcript.clear();
        // loop detector: same call set repeated
        let mut prev_sig: Option<String> = None;
        let mut repeat = 0u64;

        let final_result = loop {
            if started.elapsed().as_secs() > self.cfg.max_duration_min * 60 {
                break "⏰ лимит времени (2 ч) достигнут".to_string();
            }
            step += 1;

            // V2.7: timer-hook tick (V2.8: last_fire persisted in Plugin)
            crate::plugins::run_timers(
                &mut self.plugins,
                crate::plugins::now_sec(),
                &hook_env(goal, step, &[], ""),
            );

            crate::plugins::run_plugins(
                &self.plugins,
                "before_step",
                &hook_env(goal, step, &[], ""),
            );

            let prompt = self.build_prompt(goal, mem, &transcript);
            let calls = match self.model.decide(&prompt) {
                AgentDecision::Reply(text) => break format!("✅ {text}"),
                AgentDecision::Tools(calls) => calls,
            };

            if calls.is_empty() {
                break format!("готово за {step} шагов: модель действий не предложила");
            }

            // loop detector (V1.3): same call N times in a row → stop
            let sig = calls
                .iter()
                .map(|c| {
                    format!(
                        "{}:{}",
                        c.tool,
                        serde_json::to_string(&c.args).unwrap_or_default()
                    )
                })
                .collect::<Vec<_>>()
                .join("|");
            if Some(&sig) == prev_sig.as_ref() {
                repeat += 1;
            } else {
                repeat = 0;
                prev_sig = Some(sig);
            }
            if repeat >= 3 {
                break format!(
                    "⏹ зацикливание: одинаковый вызов {} раз подряд — остановлено",
                    repeat + 1
                );
            }

            let mut results = Vec::new();
            for c in &calls {
                if self.mode == Mode::Plan && c.is_write() {
                    results.push(ToolResult {
                        tool: c.tool.clone(),
                        ok: false,
                        summary: "plan-режим (read-only): отказ, предложи план".into(),
                    });
                    continue;
                }
                let granted = self.mode_is_auto_or_bypass() || self.approve || !c.dangerous;
                if c.dangerous && !granted {
                    results.push(ToolResult {
                        tool: c.tool.clone(),
                        ok: false,
                        summary: "отклонено оператором (dangerous; запусти с --yes)".into(),
                    });
                    continue;
                }
                results.push(self.run_tool(c, mem));
            }

            let summary = self.model.compress(&results);
            let tools: Vec<String> = calls.iter().map(|c| c.tool.clone()).collect();
            crate::plugins::run_plugins(
                &self.plugins,
                "after_step",
                &hook_env(goal, step, &tools, &summary),
            );
            transcript.push(format!("[step {step}] {} → {summary}", tools.join(",")));
            self.last_transcript = transcript.clone();

            // P3B: sliding-window reflection — every N steps, not each (flag)
            if self.cfg.reflection && step.is_multiple_of(self.cfg.reflection_every) {
                self.reflect_once(mem, &transcript);
            }

            if self.done(&summary) {
                break format!("завершено за {step} шагов; последний шаг: {summary}");
            }
        };

        // P3B: final flush — do not lose the trailing window
        if self.cfg.reflection {
            self.reflect_once(mem, &self.last_transcript);
        }

        // V2.3: on_done hook (fire-and-forget, env with the result)
        crate::plugins::run_plugins(
            &self.plugins,
            "on_done",
            &hook_env(goal, step, &[], &final_result),
        );

        final_result
    }

    /// P3B: single reflection call over the last `window` steps.
    fn reflect_once(&self, mem: &mut Memory, transcript: &[String]) {
        let window: String = transcript
            .iter()
            .rev()
            .take(self.cfg.reflection_window as usize)
            .collect::<Vec<_>>()
            .into_iter()
            .rev()
            .cloned()
            .collect::<Vec<_>>()
            .join("\n");
        if window.trim().is_empty() {
            return;
        }
        for item in self.model.reflect(&window) {
            match item {
                ReflectionItem::Set {
                    key,
                    value,
                    pinned,
                    keywords,
                } => {
                    mem.set_fact(&key, &value, pinned, keywords);
                }
                ReflectionItem::Note {
                    content,
                    tags,
                    kind,
                } => {
                    mem.add_note(&content, tags, kind);
                }
            }
        }
        // Consolidator: repeated notes (>=3 sharing a tag) → lesson + procedure
        let n = mem.consolidate();
        if n > 0 {
            eprintln!("[memory] консолидировано уроков: {n}");
            // V3.0: LLM distillation of a procedure from the cluster (fallback — heuristic)
            if let Some(p) = mem.procedures.last().cloned() {
                let notes_text: String = mem
                    .notes
                    .iter()
                    .filter(|x| p.parents.contains(&x.id))
                    .map(|x| x.content.clone())
                    .collect::<Vec<_>>()
                    .join("\n");
                if !notes_text.is_empty() {
                    if let Some((act, steps)) =
                        self.model.distill_procedure(&p.tags.join(","), &notes_text)
                    {
                        mem.set_procedure(p.id, &act, steps);
                        eprintln!("[memory] процедура #{} дистиллирована LLM", p.id);
                    }
                }
            }
            // V3.1: LLM distillation of a lesson from the same cluster
            if let Some(l) = mem.lessons.last().cloned() {
                let lnotes: String = mem
                    .notes
                    .iter()
                    .filter(|x| l.parents.contains(&x.id))
                    .map(|x| x.content.clone())
                    .collect::<Vec<_>>()
                    .join("\n");
                if !lnotes.is_empty() {
                    if let Some((act, principle)) =
                        self.model.distill_lesson(&l.tags.join(","), &lnotes)
                    {
                        mem.set_lesson(l.id, &act, &principle);
                        eprintln!("[memory] урок #{} дистиллирован LLM", l.id);
                    }
                }
            }
        }
    }

    fn build_prompt(&self, goal: &str, mem: &Memory, transcript: &[String]) -> String {
        let mut p = String::from("### system\nlocal-first agent\n\n");
        p.push_str(&format!("### cwd\n{}\n\n", self.cwd));
        p.push_str(&crate::skills::skills_index(&self.skills));
        p.push_str(&mem.profile_block(goal));
        p.push_str(&mem.lessons_block(goal));
        p.push_str(&mem.procedures_block(goal));
        p.push_str(&mem.memory_index());
        p.push_str(&format!("### goal\n{goal}\n\n"));
        p.push_str("### transcript (последние шаги)\n");
        if transcript.is_empty() {
            p.push_str("(пусто)\n");
        } else {
            for t in transcript.iter().rev().take(8) {
                p.push('\t');
                p.push_str(t);
                p.push('\n');
            }
        }
        p
    }

    fn run_tool(&self, c: &ToolCall, mem: &mut Memory) -> ToolResult {
        let name = c.tool.as_str();
        match name {
            "memory.set" => {
                let k = c.args["key"].as_str().unwrap_or("?").to_string();
                let v = c.args["value"].as_str().unwrap_or("").to_string();
                let pinned = c.args["pinned"].as_bool().unwrap_or(false);
                let keywords = c.args["keywords"]
                    .as_array()
                    .map(|a| {
                        a.iter()
                            .filter_map(|x| x.as_str().map(String::from))
                            .collect()
                    })
                    .unwrap_or_default();
                mem.set_fact(&k, &v, pinned, keywords);
                ToolResult {
                    tool: name.into(),
                    ok: true,
                    summary: format!("profile: {k} сохранён"),
                }
            }
            "memory.note" => {
                let content = c.args["content"].as_str().unwrap_or("").to_string();
                let tags = c.args["tags"]
                    .as_array()
                    .map(|a| {
                        a.iter()
                            .filter_map(|x| x.as_str().map(String::from))
                            .collect()
                    })
                    .unwrap_or_default();
                let kind = match c.args["kind"].as_str().unwrap_or("knowledge") {
                    "event" => NoteKind::Event,
                    "behavior" => NoteKind::Behavior,
                    "skill" => NoteKind::Skill,
                    _ => NoteKind::Knowledge,
                };
                let id = mem.add_note(&content, tags, kind);
                ToolResult {
                    tool: name.into(),
                    ok: true,
                    summary: format!("note #{id} сохранена"),
                }
            }
            "memory.lesson" => {
                let activation = c.args["activation"].as_str().unwrap_or("").to_string();
                let principle = c.args["principle"].as_str().unwrap_or("").to_string();
                let tags = c.args["tags"]
                    .as_array()
                    .map(|a| {
                        a.iter()
                            .filter_map(|x| x.as_str().map(String::from))
                            .collect()
                    })
                    .unwrap_or_default();
                let id = mem.add_lesson(&activation, &principle, tags, vec![]);
                ToolResult {
                    tool: name.into(),
                    ok: true,
                    summary: format!("lesson #{id} сохранён"),
                }
            }
            "memory.recall" => {
                // P3A: query rewriter — expand short referential queries from goal
                let mut q = c.args["query"].as_str().unwrap_or("").to_string();
                if self.cfg.rewriter && is_referential(&q) && !self.goal.is_empty() {
                    let anchor: String = self.goal.split_whitespace().collect::<Vec<_>>().join(" ");
                    q = format!("{anchor} {q}");
                }
                let hits = mem.recall_hybrid(&q, 3);
                let summary = if hits.is_empty() {
                    "ничего не найдено".into()
                } else {
                    hits.iter()
                        .map(|n| {
                            format!(
                                "#{} {}",
                                n.id,
                                n.content.chars().take(80).collect::<String>()
                            )
                        })
                        .collect::<Vec<_>>()
                        .join(" | ")
                };
                ToolResult {
                    tool: name.into(),
                    ok: true,
                    summary,
                }
            }
            "file.read" => {
                let path = c.args["path"].as_str().unwrap_or("").to_string();
                self.read_file(&path)
            }
            "file.write" => {
                let path = c.args["path"].as_str().unwrap_or("").to_string();
                let content = c.args["content"].as_str().unwrap_or("").to_string();
                self.write_file(&path, &content)
            }
            "shell" => {
                let cmd = c.args["command"].as_str().unwrap_or("").to_string();
                self.run_shell(&cmd)
            }
            "http.get" => {
                let url = c.args["url"].as_str().unwrap_or("").to_string();
                self.http_get(&url)
            }
            "browser.get" => {
                let url = c.args["url"].as_str().unwrap_or("").to_string();
                self.browser_get(&url)
            }
            "browser.navigate" => {
                let url = c.args["url"].as_str().unwrap_or("").to_string();
                if !is_safe_url(&url) {
                    return ToolResult {
                        tool: "browser.navigate".into(),
                        ok: false,
                        summary: "заблокировано: SSRF-guard (private/loopback/non-http)".into(),
                    };
                }
                match crate::browser::navigate(&url) {
                    Ok(t) => ToolResult {
                        tool: "browser.navigate".into(),
                        ok: true,
                        summary: format!("TITLE: {t}"),
                    },
                    Err(e) => ToolResult {
                        tool: "browser.navigate".into(),
                        ok: false,
                        summary: e,
                    },
                }
            }
            "browser.click" => {
                let sel = c.args["selector"].as_str().unwrap_or("").to_string();
                match crate::browser::click(&sel) {
                    Ok(r) => ToolResult {
                        tool: "browser.click".into(),
                        ok: true,
                        summary: r,
                    },
                    Err(e) => ToolResult {
                        tool: "browser.click".into(),
                        ok: false,
                        summary: e,
                    },
                }
            }
            "browser.type" => {
                let sel = c.args["selector"].as_str().unwrap_or("").to_string();
                let text = c.args["text"].as_str().unwrap_or("").to_string();
                match crate::browser::type_text(&sel, &text) {
                    Ok(r) => ToolResult {
                        tool: "browser.type".into(),
                        ok: true,
                        summary: r,
                    },
                    Err(e) => ToolResult {
                        tool: "browser.type".into(),
                        ok: false,
                        summary: e,
                    },
                }
            }
            "browser.snapshot" => match crate::browser::snapshot() {
                Ok(r) => {
                    let clipped: String = r.chars().take(1500).collect();
                    ToolResult {
                        tool: "browser.snapshot".into(),
                        ok: true,
                        summary: clipped,
                    }
                }
                Err(e) => ToolResult {
                    tool: "browser.snapshot".into(),
                    ok: false,
                    summary: e,
                },
            },
            "browser.screenshot" => {
                let path = c.args["path"].as_str().unwrap_or("shot.png").to_string();
                match crate::browser::screenshot(&path) {
                    Ok(r) => ToolResult {
                        tool: "browser.screenshot".into(),
                        ok: true,
                        summary: r,
                    },
                    Err(e) => ToolResult {
                        tool: "browser.screenshot".into(),
                        ok: false,
                        summary: e,
                    },
                }
            }
            "browser.eval" => {
                let expr = c.args["expression"].as_str().unwrap_or("").to_string();
                match crate::browser::cdp_eval(&expr) {
                    Ok(r) => ToolResult {
                        tool: "browser.eval".into(),
                        ok: true,
                        summary: r.chars().take(1000).collect(),
                    },
                    Err(e) => ToolResult {
                        tool: "browser.eval".into(),
                        ok: false,
                        summary: e,
                    },
                }
            }
            "browser.flow" => {
                let steps: Vec<crate::browser::FlowStep> =
                    serde_json::from_value(c.args["steps"].clone()).unwrap_or_default();
                if steps.is_empty() {
                    return ToolResult {
                        tool: "browser.flow".into(),
                        ok: false,
                        summary: "steps пуст".into(),
                    };
                }
                match crate::browser::flow(&steps) {
                    Ok(r) => ToolResult {
                        tool: "browser.flow".into(),
                        ok: true,
                        summary: r.chars().take(1500).collect(),
                    },
                    Err(e) => ToolResult {
                        tool: "browser.flow".into(),
                        ok: false,
                        summary: e,
                    },
                }
            }
            "skill.view" => {
                let name = c.args["name"].as_str().unwrap_or("").to_string();
                match crate::skills::find_skill(&self.skills, &name) {
                    Some(s) => ToolResult {
                        tool: "skill.view".into(),
                        ok: true,
                        summary: format!(
                            "## {} v{} (dangerous: {})\n{}\n\n{}",
                            s.name,
                            s.version,
                            s.dangerous,
                            s.description,
                            s.body.chars().take(1200).collect::<String>()
                        ),
                    },
                    None => ToolResult {
                        tool: "skill.view".into(),
                        ok: false,
                        summary: format!("скилл не найден: {name}"),
                    },
                }
            }
            "mcp.tools" => {
                let name = c.args["server"].as_str().unwrap_or("").to_string();
                let sdir = agent_state_dir();
                let Some(srv) = crate::mcp::load_servers(&sdir)
                    .iter()
                    .find(|x| x.name == name)
                    .cloned()
                else {
                    return ToolResult {
                        tool: "mcp.tools".into(),
                        ok: false,
                        summary: format!("MCP-сервер '{name}' не найден"),
                    };
                };
                match crate::mcp::McpClient::connect(&srv) {
                    Ok(mut c) => {
                        let tools = c.tools().unwrap_or_default();
                        let summary = if tools.is_empty() {
                            "нет инструментов".into()
                        } else {
                            tools
                                .iter()
                                .map(|t| {
                                    format!(
                                        "{}: {}",
                                        t.name,
                                        t.description.chars().take(60).collect::<String>()
                                    )
                                })
                                .collect::<Vec<_>>()
                                .join("\n")
                        };
                        ToolResult {
                            tool: "mcp.tools".into(),
                            ok: true,
                            summary,
                        }
                    }
                    Err(e) => ToolResult {
                        tool: "mcp.tools".into(),
                        ok: false,
                        summary: e,
                    },
                }
            }
            "mcp.call" => {
                let name = c.args["server"].as_str().unwrap_or("").to_string();
                let tool = c.args["tool"].as_str().unwrap_or("").to_string();
                let j = c
                    .args
                    .get("args")
                    .cloned()
                    .unwrap_or(serde_json::Value::Object(Default::default()));
                let sdir = agent_state_dir();
                let Some(srv) = crate::mcp::load_servers(&sdir)
                    .iter()
                    .find(|x| x.name == name)
                    .cloned()
                else {
                    return ToolResult {
                        tool: "mcp.call".into(),
                        ok: false,
                        summary: format!("MCP-сервер '{name}' не найден"),
                    };
                };
                match crate::mcp::McpClient::connect(&srv) {
                    Ok(mut c) => match c.call_tool(&tool, &j) {
                        Ok(out) => ToolResult {
                            tool: "mcp.call".into(),
                            ok: true,
                            summary: out.chars().take(1200).collect(),
                        },
                        Err(e) => ToolResult {
                            tool: "mcp.call".into(),
                            ok: false,
                            summary: e,
                        },
                    },
                    Err(e) => ToolResult {
                        tool: "mcp.call".into(),
                        ok: false,
                        summary: e,
                    },
                }
            }
            "skill.run" => {
                let name = c.args["name"].as_str().unwrap_or("").to_string();
                let script = c.args["script"].as_str().unwrap_or("").to_string();
                let args: Vec<String> = c.args["args"]
                    .as_array()
                    .map(|a| {
                        a.iter()
                            .filter_map(|x| x.as_str().map(String::from))
                            .collect()
                    })
                    .unwrap_or_default();
                match crate::skills::find_skill(&self.skills, &name) {
                    Some(s) => match crate::skills::run_script(s, &script, &args) {
                        Ok(r) => ToolResult {
                            tool: "skill.run".into(),
                            ok: true,
                            summary: r,
                        },
                        Err(e) => ToolResult {
                            tool: "skill.run".into(),
                            ok: false,
                            summary: e,
                        },
                    },
                    None => ToolResult {
                        tool: "skill.run".into(),
                        ok: false,
                        summary: format!("скилл не найден: {name}"),
                    },
                }
            }
            "web.search" => {
                let q = c.args["query"].as_str().unwrap_or("").to_string();
                self.web_search(&q)
            }
            _ => ToolResult {
                tool: name.into(),
                ok: false,
                summary: format!("неизвестный инструмент: {name}"),
            },
        }
    }

    fn resolve(&self, path: &str) -> std::path::PathBuf {
        let p = std::path::Path::new(path);
        if p.is_absolute() {
            p.to_path_buf()
        } else {
            std::path::Path::new(&self.cwd).join(p)
        }
    }

    fn read_file(&self, path: &str) -> ToolResult {
        let full = self.resolve(path);
        match std::fs::read_to_string(&full) {
            Ok(body) => {
                let size = body.len();
                let clipped: String = body.chars().take(2000).collect();
                let more = if size > 2000 {
                    "… [обрезано]"
                } else {
                    ""
                };
                ToolResult {
                    tool: "file.read".into(),
                    ok: true,
                    summary: format!("{} ({} байт):\n{}{}", full.display(), size, clipped, more),
                }
            }
            Err(e) => ToolResult {
                tool: "file.read".into(),
                ok: false,
                summary: format!("не прочитан {}: {e}", full.display()),
            },
        }
    }

    fn write_file(&self, path: &str, content: &str) -> ToolResult {
        let full = self.resolve(path);
        if let Some(parent) = full.parent() {
            let _ = std::fs::create_dir_all(parent);
        }
        match std::fs::write(&full, content) {
            Ok(()) => ToolResult {
                tool: "file.write".into(),
                ok: true,
                summary: format!("записан {} ({} байт)", full.display(), content.len()),
            },
            Err(e) => ToolResult {
                tool: "file.write".into(),
                ok: false,
                summary: format!("не записан {}: {e}", full.display()),
            },
        }
    }

    fn run_shell(&self, cmd: &str) -> ToolResult {
        // V3.5: sandbox — dangerous patterns are blocked even with --yes
        let low = cmd.to_lowercase();
        let dangerous_patterns = [
            "rm -rf /",
            "sudo ",
            "su ",
            "mkfs.",
            "dd if=/dev/zero of=/dev",
            "chmod -r 777 /",
            ":(){",
            "> /dev/sda",
            "shutdown",
            "reboot",
            "init 0",
            "curl | sh",
            "wget | sh",
            "chown -r",
        ];
        if let Some(p) = dangerous_patterns.iter().find(|p| low.contains(*p)) {
            return ToolResult {
                tool: "shell".into(),
                ok: false,
                summary: format!("sandbox: команда содержит опасный паттерн '{p}' — отклонено"),
            };
        }
        match std::process::Command::new("sh").arg("-c").arg(cmd).output() {
            Ok(out) => {
                let mut s = String::from_utf8_lossy(&out.stdout).to_string();
                let err = String::from_utf8_lossy(&out.stderr).to_string();
                if !err.is_empty() {
                    s.push_str(&format!("\n[stderr] {err}"));
                }
                let clipped: String = s.chars().take(1500).collect();
                ToolResult {
                    tool: "shell".into(),
                    ok: out.status.success(),
                    summary: format!("exit={}:\n{clipped}", out.status.code().unwrap_or(-1)),
                }
            }
            Err(e) => ToolResult {
                tool: "shell".into(),
                ok: false,
                summary: format!("не выполнен: {e}"),
            },
        }
    }

    /// http.get — fetch a page, SSRF-guarded (no private/loopback), http/https only.
    fn http_get(&self, url: &str) -> ToolResult {
        if !is_safe_url(url) {
            return ToolResult {
                tool: "http.get".into(),
                ok: false,
                summary: "заблокировано: SSRF-guard (private/loopback/non-http)".into(),
            };
        }
        let client = reqwest::blocking::Client::builder()
            .timeout(std::time::Duration::from_secs(20))
            .build()
            .unwrap_or_default();
        match client.get(url).send() {
            Ok(resp) => {
                let status = resp.status();
                let body = resp.text().unwrap_or_default();
                let clipped: String = body.chars().take(2500).collect();
                let more = if body.len() > 2500 {
                    "… [обрезано]"
                } else {
                    ""
                };
                ToolResult {
                    tool: "http.get".into(),
                    ok: status.is_success(),
                    summary: format!("HTTP {status} ({} байт):\n{clipped}{more}", body.len()),
                }
            }
            Err(e) => ToolResult {
                tool: "http.get".into(),
                ok: false,
                summary: format!("http.get {url}: {e}"),
            },
        }
    }

    /// web.search — DuckDuckGo HTML search (no key), extracts title+url.
    fn web_search(&self, query: &str) -> ToolResult {
        // V3.0: provider from ARGUS_SEARCH_PROVIDER (ddg|brave|searxng), fallback ddg
        let provider = std::env::var("ARGUS_SEARCH_PROVIDER").unwrap_or_else(|_| "ddg".into());
        match provider.as_str() {
            "brave" => self.search_brave(query),
            "searxng" => self.search_searxng(query),
            _ => self.search_ddg(query),
        }
    }

    fn search_ddg(&self, query: &str) -> ToolResult {
        let client = reqwest::blocking::Client::builder()
            .timeout(std::time::Duration::from_secs(20))
            .build()
            .unwrap_or_default();
        let url = format!("https://html.duckduckgo.com/html/?q={}", urlencode(query));
        let resp = match client
            .get(&url)
            .header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) ARGUS-OS1")
            .send()
        {
            Ok(r) => r,
            Err(e) => {
                return ToolResult {
                    tool: "web.search".into(),
                    ok: false,
                    summary: format!("web.search: {e}"),
                }
            }
        };
        let body = resp.text().unwrap_or_default();
        let results = parse_ddg(&body, 5);
        if results.is_empty() {
            return ToolResult {
                tool: "web.search".into(),
                ok: false,
                summary: "web.search: результатов не найдено (или DDG недоступен)".into(),
            };
        }
        ToolResult {
            tool: "web.search".into(),
            ok: true,
            summary: results.join("\n"),
        }
    }

    /// Brave Search API (key ARGUS_BRAVE_API_KEY).
    fn search_brave(&self, query: &str) -> ToolResult {
        let key = std::env::var("ARGUS_BRAVE_API_KEY").unwrap_or_default();
        if key.is_empty() {
            return self.search_ddg(query); // fallback
        }
        let client = reqwest::blocking::Client::builder()
            .timeout(std::time::Duration::from_secs(20))
            .build()
            .unwrap_or_default();
        let url = format!(
            "https://api.search.brave.com/res/v1/web/search?q={}&count=5",
            urlencode(query)
        );
        let resp = match client
            .get(&url)
            .header("X-Subscription-Token", &key)
            .header("Accept", "application/json")
            .send()
        {
            Ok(r) => r,
            Err(e) => {
                return ToolResult {
                    tool: "web.search".into(),
                    ok: false,
                    summary: format!("brave: {e}"),
                }
            }
        };
        let v: serde_json::Value = match resp.json() {
            Ok(v) => v,
            Err(e) => {
                return ToolResult {
                    tool: "web.search".into(),
                    ok: false,
                    summary: format!("brave: {e}"),
                }
            }
        };
        let mut out = Vec::new();
        if let Some(arr) = v
            .get("web")
            .and_then(|w| w.get("results"))
            .and_then(|r| r.as_array())
        {
            for r in arr.iter().take(5) {
                let title = r.get("title").and_then(|x| x.as_str()).unwrap_or("");
                let url = r.get("url").and_then(|x| x.as_str()).unwrap_or("");
                out.push(format!("• {title}\n  {url}"));
            }
        }
        if out.is_empty() {
            return ToolResult {
                tool: "web.search".into(),
                ok: false,
                summary: "brave: пусто".into(),
            };
        }
        ToolResult {
            tool: "web.search".into(),
            ok: true,
            summary: out.join("\n"),
        }
    }

    /// SearXNG (self-hosted, URL ARGUS_SEARXNG_URL).
    fn search_searxng(&self, query: &str) -> ToolResult {
        let base = std::env::var("ARGUS_SEARXNG_URL").unwrap_or_default();
        if base.is_empty() {
            return self.search_ddg(query); // fallback
        }
        let client = reqwest::blocking::Client::builder()
            .timeout(std::time::Duration::from_secs(20))
            .build()
            .unwrap_or_default();
        let url = format!(
            "{}/search?q={}&format=json",
            base.trim_end_matches('/'),
            urlencode(query)
        );
        let resp = match client.get(&url).send() {
            Ok(r) => r,
            Err(e) => {
                return ToolResult {
                    tool: "web.search".into(),
                    ok: false,
                    summary: format!("searxng: {e}"),
                }
            }
        };
        let v: serde_json::Value = match resp.json() {
            Ok(v) => v,
            Err(e) => {
                return ToolResult {
                    tool: "web.search".into(),
                    ok: false,
                    summary: format!("searxng: {e}"),
                }
            }
        };
        let mut out = Vec::new();
        if let Some(arr) = v.get("results").and_then(|r| r.as_array()) {
            for r in arr.iter().take(5) {
                let title = r.get("title").and_then(|x| x.as_str()).unwrap_or("");
                let url = r.get("url").and_then(|x| x.as_str()).unwrap_or("");
                out.push(format!("• {title}\n  {url}"));
            }
        }
        if out.is_empty() {
            return ToolResult {
                tool: "web.search".into(),
                ok: false,
                summary: "searxng: пусто".into(),
            };
        }
        ToolResult {
            tool: "web.search".into(),
            ok: true,
            summary: out.join("\n"),
        }
    }

    /// browser.get — real browser rendering via headless Chrome (--dump-dom).
    /// JS executes; SSRF-guard same as http.get. Click/type — V1.4 (CDP).
    fn browser_get(&self, url: &str) -> ToolResult {
        if !is_safe_url(url) {
            return ToolResult {
                tool: "browser.get".into(),
                ok: false,
                summary: "заблокировано: SSRF-guard (private/loopback/non-http)".into(),
            };
        }
        let candidates = [
            "google-chrome",
            "google-chrome-stable",
            "chromium",
            "chromium-browser",
        ];
        let Some(chrome) = candidates.iter().find(|c| which(c)) else {
            return ToolResult {
                tool: "browser.get".into(),
                ok: false,
                summary: "браузер не найден (нужен google-chrome/chromium)".into(),
            };
        };
        let out = match std::process::Command::new(chrome)
            .args([
                "--headless",
                "--disable-gpu",
                "--no-sandbox",
                "--user-data-dir=/tmp/argus-dumpdom-profile",
                "--virtual-time-budget=8000",
                "--dump-dom",
                url,
            ])
            .output()
        {
            Ok(o) => o,
            Err(e) => {
                return ToolResult {
                    tool: "browser.get".into(),
                    ok: false,
                    summary: format!("browser.get: {e}"),
                }
            }
        };
        if !out.status.success() {
            return ToolResult {
                tool: "browser.get".into(),
                ok: false,
                summary: format!("browser.get: chrome exit {:?}", out.status.code()),
            };
        }
        let html = String::from_utf8_lossy(&out.stdout).to_string();
        let title = extract_title(&html).unwrap_or_else(|| "(нет title)".into());
        let text = html_to_text(&html);
        let clipped: String = text.chars().take(1800).collect();
        let more = if text.len() > 1800 {
            "… [обрезано]"
        } else {
            ""
        };
        ToolResult {
            tool: "browser.get".into(),
            ok: true,
            summary: format!("TITLE: {title}\n{clipped}{more}"),
        }
    }

    fn mode_is_auto_or_bypass(&self) -> bool {
        matches!(self.mode, Mode::Auto | Mode::Bypass)
    }

    fn done(&self, summary: &str) -> bool {
        summary.to_lowercase().contains("done") || summary.to_lowercase().contains("готово")
    }
}

/// V3.6: state directory (for MCP servers).
pub fn agent_state_dir() -> std::path::PathBuf {
    std::env::var("ARGUS_STATE_DIR")
        .map(std::path::PathBuf::from)
        .unwrap_or_else(|_| {
            std::path::PathBuf::from(std::env::var("HOME").unwrap_or_default()).join(".argus-agent")
        })
}

/// V2.3: env context for hooks.
fn hook_env(goal: &str, step: u64, tools: &[String], summary: &str) -> Vec<(&'static str, String)> {
    vec![
        ("ARGUS_GOAL", goal.to_string()),
        ("ARGUS_STEP", step.to_string()),
        ("ARGUS_TOOLS", tools.join(",")),
        ("ARGUS_SUMMARY", summary.to_string()),
    ]
}

impl ToolCall {
    fn is_write(&self) -> bool {
        matches!(
            self.tool.as_str(),
            "file.write" | "shell" | "memory.set" | "memory.note" | "memory.lesson"
        )
    }
}

/// P3A: "short referential query" heuristic (like Atomic MEMORY_FABRIC v2.5 Phase A).
fn is_referential(q: &str) -> bool {
    let t = q.trim();
    if t.is_empty() {
        return false;
    }
    let words: Vec<&str> = t.split_whitespace().collect();
    let short = words.len() <= 5;
    let starts_conj = ["а ", "и ", "но ", "и про ", "and ", "but "]
        .iter()
        .any(|c| t.to_lowercase().starts_with(c));
    let pronouns = [
        "это",
        "этот",
        "она",
        "он",
        "они",
        "там",
        "туда",
        "про то",
        "тот",
        "который",
        "его",
        "её",
    ]
    .iter()
    .any(|w| t.to_lowercase().contains(w));
    short || starts_conj || pronouns
}

/// SSRF guard: http/https only, private/loopback hosts blocked.
fn is_safe_url(url: &str) -> bool {
    let lower = url.to_lowercase();
    if !(lower.starts_with("http://") || lower.starts_with("https://")) {
        return false;
    }
    let host = match url.split("://").nth(1) {
        Some(rest) => rest.split(['/', '?', '#']).next().unwrap_or(""),
        None => return false,
    };
    let host = host.trim_start_matches('[').trim_end_matches(']'); // ipv6 [::1]
    if host.is_empty() {
        return false;
    }
    if host.eq_ignore_ascii_case("localhost") || host.ends_with(".local") {
        return false;
    }
    if let Some(ip) = host.split(':').next() {
        let oct: Vec<&str> = ip.split('.').collect();
        if oct.len() == 4 {
            let nums: Vec<u32> = oct.iter().filter_map(|o| o.parse().ok()).collect();
            if nums.len() == 4
                && (nums[0] == 10
                    || nums[0] == 127
                    || nums[0] == 0
                    || (nums[0] == 192 && nums[1] == 168)
                    || (nums[0] == 172 && (16..=31).contains(&nums[1]))
                    || (nums[0] == 169 && nums[1] == 254))
            {
                return false;
            }
        }
    }
    if host == "::1"
        || host.starts_with("fe80:")
        || host.starts_with("fc")
        || host.starts_with("fd")
    {
        return false;
    }
    // V3.5: DNS resolve — block private IP even if the name bypasses the string check
    use std::net::ToSocketAddrs;
    if let Ok(addrs) = (host, 80u16).to_socket_addrs() {
        for a in addrs {
            let ip = a.ip();
            let blocked = match ip {
                std::net::IpAddr::V4(v4) => {
                    v4.is_loopback()
                        || v4.is_unspecified()
                        || v4.is_multicast()
                        || v4.octets()[0] == 10
                        || v4.octets()[0] == 127
                        || (v4.octets()[0] == 192 && v4.octets()[1] == 168)
                        || (v4.octets()[0] == 172 && (16..=31).contains(&v4.octets()[1]))
                        || (v4.octets()[0] == 169 && v4.octets()[1] == 254)
                }
                std::net::IpAddr::V6(v6) => {
                    v6.is_loopback()
                        || v6.is_unspecified()
                        || v6.is_multicast()
                        || v6.segments()[0] & 0xffc0 == 0xfe80
                }
            };
            if blocked {
                return false;
            }
        }
    }
    true
}

fn urlencode(s: &str) -> String {
    let mut out = String::new();
    for b in s.as_bytes() {
        match *b {
            b'A'..=b'Z' | b'a'..=b'z' | b'0'..=b'9' | b'-' | b'_' | b'.' | b'~' => {
                out.push(*b as char)
            }
            b' ' => out.push('+'),
            _ => out.push_str(&format!("%{:02X}", b)),
        }
    }
    out
}

/// Checks whether a binary exists in PATH.
fn which(cmd: &str) -> bool {
    std::process::Command::new("which")
        .arg(cmd)
        .output()
        .map(|o| o.status.success())
        .unwrap_or(false)
}

/// Extracts <title>...</title> from HTML.
fn extract_title(html: &str) -> Option<String> {
    let start = html.find("<title>")? + 7;
    let end = html[start..].find("</title>")? + start;
    Some(html[start..end].trim().to_string())
}

/// Crude visible-text extraction: strip scripts/styles/tags.
fn html_to_text(html: &str) -> String {
    let mut out = String::new();
    let mut skip = 0usize;
    let bytes = html.as_bytes();
    let mut i = 0;
    while i < bytes.len() {
        if bytes[i] == b'<' {
            let tag_end = html[i..]
                .find('>')
                .map(|d| i + d + 1)
                .unwrap_or(bytes.len());
            let tag = &html[i..tag_end];
            let low = tag.to_lowercase();
            if low.starts_with("<script")
                || low.starts_with("<style")
                || low.starts_with("<noscript")
            {
                skip = tag_end;
            }
            i = tag_end;
            continue;
        }
        if skip > 0 && i >= skip {
            skip = 0;
        }
        if skip == 0 {
            out.push(html.as_bytes()[i] as char);
        }
        i += 1;
    }
    // collapse extra whitespace/newlines
    let cleaned: Vec<String> = out
        .split_whitespace()
        .map(|s| s.to_string())
        .collect::<Vec<_>>()
        .chunks(12)
        .map(|c| c.join(" "))
        .collect();
    cleaned.join("\n")
}

/// Parses DDG HTML results: `<a class="result__a" href="...">title</a>`.
fn parse_ddg(body: &str, max: usize) -> Vec<String> {
    let mut out = Vec::new();
    let mut search_from = 0usize;
    while out.len() < max {
        let Some(rel) = body[search_from..].find("result__a") else {
            break;
        };
        let a_start = search_from + rel;
        // href="..."
        let Some(href_rel) = body[a_start..].find("href=\"") else {
            break;
        };
        let h0 = a_start + href_rel + 6;
        let Some(h1_rel) = body[h0..].find('\"') else {
            break;
        };
        let href = &body[h0..h0 + h1_rel];
        // title: after >
        let Some(gt_rel) = body[a_start..].find('>') else {
            break;
        };
        let t0 = a_start + gt_rel + 1;
        let Some(lt_rel) = body[t0..].find('<') else {
            break;
        };
        let title = body[t0..t0 + lt_rel].trim();
        if !href.is_empty() && !title.is_empty() {
            out.push(format!("• {title}\n  {href}"));
        }
        search_from = t0 + lt_rel;
    }
    out
}

// ============================================================================
// LlmModel — OpenAI-compatible HTTP client (Ollama / LM Studio / llama-server)
// ============================================================================

#[derive(Debug, Clone)]
pub struct LlmConfig {
    pub base_url: String,
    pub model: String,
    pub max_tokens: u32,
    pub temperature: f32,
}

impl Default for LlmConfig {
    fn default() -> Self {
        LlmConfig {
            base_url: "http://127.0.0.1:11434".into(),
            model: "qwen2.5:7b".into(),
            max_tokens: 2048,
            temperature: 0.2,
        }
    }
}

#[derive(Serialize)]
struct ChatRequest {
    model: String,
    messages: Vec<ChatMsg>,
    #[serde(skip_serializing_if = "Option::is_none")]
    tools: Option<Vec<ToolDef>>,
    max_tokens: u32,
    temperature: f32,
}

#[derive(Serialize, Clone)]
struct ChatMsg {
    role: String,
    content: String,
}

#[derive(Serialize, Clone)]
struct ToolDef {
    #[serde(rename = "type")]
    ty: String,
    function: FnDef,
}

#[derive(Serialize, Clone)]
struct FnDef {
    name: String,
    description: String,
    parameters: serde_json::Value,
}

#[derive(Deserialize, Debug)]
struct ChatResp {
    choices: Vec<Choice>,
}

#[derive(Deserialize, Debug)]
struct Choice {
    message: RespMessage,
}

#[derive(Deserialize, Debug)]
struct RespMessage {
    #[serde(default)]
    tool_calls: Vec<RespToolCall>,
    #[serde(default)]
    content: Option<String>,
}

#[derive(Deserialize, Debug)]
struct RespToolCall {
    function: RespFn,
}

#[derive(Deserialize, Debug)]
struct RespFn {
    name: String,
    #[serde(default)]
    arguments: String,
}

/// OpenAI-compatible model.
pub struct LlmModel {
    cfg: LlmConfig,
    client: reqwest::blocking::Client,
    tools: Vec<ToolDef>,
}

impl LlmModel {
    pub fn new(cfg: LlmConfig) -> Self {
        let client = reqwest::blocking::Client::builder()
            .timeout(std::time::Duration::from_secs(300))
            .build()
            .expect("http client");
        let tools = build_tools();
        LlmModel { cfg, client, tools }
    }

    /// Fusion: the planner splits the task into N subtasks (JSON array of strings).
    pub fn plan_subtasks(&self, goal: &str, n: usize) -> Vec<String> {
        let system = format!(
            "Ты — планировщик. Разбей задачу на {n} независимых подзадач. \
             Верни ТОЛЬКО JSON-массив строк, например [\"подзадача 1\",\"подзадача 2\"]. Никакого текста вокруг."
        );
        let messages = vec![
            ChatMsg {
                role: "system".into(),
                content: system,
            },
            ChatMsg {
                role: "user".into(),
                content: goal.to_string(),
            },
        ];
        let Some((_, content)) = self.chat(messages, false) else {
            return Vec::new();
        };
        let Some(content) = content else {
            return Vec::new();
        };
        let start = content.find('[');
        let end = content.rfind(']');
        if let (Some(s), Some(e)) = (start, end) {
            if let Ok(v) = serde_json::from_str::<serde_json::Value>(&content[s..=e]) {
                if let Some(arr) = v.as_array() {
                    let subs: Vec<String> = arr
                        .iter()
                        .filter_map(|x| x.as_str().map(String::from))
                        .filter(|s| !s.is_empty())
                        .collect();
                    if !subs.is_empty() {
                        return subs;
                    }
                }
            }
        }
        Vec::new()
    }

    fn chat(
        &self,
        messages: Vec<ChatMsg>,
        with_tools: bool,
    ) -> Option<(Vec<ToolCall>, Option<String>)> {
        let url = format!(
            "{}/v1/chat/completions",
            self.cfg.base_url.trim_end_matches('/')
        );
        let req = ChatRequest {
            model: self.cfg.model.clone(),
            messages,
            tools: if with_tools {
                Some(self.tools.clone())
            } else {
                None
            },
            max_tokens: self.cfg.max_tokens,
            temperature: self.cfg.temperature,
        };
        let resp = self.client.post(&url).json(&req).send().ok()?;
        if !resp.status().is_success() {
            eprintln!("[llm] HTTP {}", resp.status());
            return None;
        }
        let parsed: ChatResp = resp.json().ok()?;
        let msg = parsed.choices.into_iter().next()?.message;
        let mut calls = Vec::new();
        for tc in msg.tool_calls {
            let args: serde_json::Value =
                serde_json::from_str(&tc.function.arguments).unwrap_or(serde_json::Value::Null);
            let dangerous = matches!(tc.function.name.as_str(), "shell" | "file.write");
            calls.push(ToolCall {
                tool: tc.function.name,
                args,
                dangerous,
            });
        }
        Some((calls, msg.content))
    }
}

impl Model for LlmModel {
    fn decide(&self, prompt: &str) -> AgentDecision {
        let messages = vec![
            ChatMsg {
                role: "system".into(),
                content: SYSTEM_PROMPT.to_string(),
            },
            ChatMsg {
                role: "user".into(),
                content: prompt.to_string(),
            },
        ];
        match self.chat(messages, true) {
            Some((calls, _)) if !calls.is_empty() => AgentDecision::Tools(calls),
            Some((_, Some(content))) => {
                // V1.1 recover layer: the model printed calls as text → recognize and run them
                if let Some(calls) = recover_text_calls(&content) {
                    AgentDecision::Tools(calls)
                } else {
                    AgentDecision::Reply(content)
                }
            }
            Some((_, None)) => AgentDecision::Reply("(пустой ответ)".into()),
            None => AgentDecision::Reply("(ошибка LLM — соединение/таймаут)".into()),
        }
    }

    fn compress(&self, results: &[ToolResult]) -> String {
        results
            .iter()
            .map(|r| {
                let s: String = r.summary.chars().take(220).collect();
                format!("{}: {}", r.tool, s)
            })
            .collect::<Vec<_>>()
            .join(" || ")
    }

    fn reflect(&self, window: &str) -> Vec<ReflectionItem> {
        let messages = vec![
            ChatMsg {
                role: "system".into(),
                content: REFLECT_PROMPT.to_string(),
            },
            ChatMsg {
                role: "user".into(),
                content: window.to_string(),
            },
        ];
        let Ok(resp) = self
            .client
            .post(format!(
                "{}/v1/chat/completions",
                self.cfg.base_url.trim_end_matches('/')
            ))
            .json(&ChatRequest {
                model: self.cfg.model.clone(),
                messages,
                tools: None,
                max_tokens: 1024,
                temperature: 0.0,
            })
            .send()
        else {
            return Vec::new();
        };
        let Ok(parsed) = resp.json::<ChatResp>() else {
            return Vec::new();
        };
        let content = parsed
            .choices
            .into_iter()
            .next()
            .and_then(|c| c.message.content)
            .unwrap_or_default();
        crate::memory::parse_reflection(&content)
            .into_iter()
            .map(|a| match a {
                crate::memory::ReflectionAction::Set {
                    key,
                    value,
                    pinned,
                    keywords,
                } => ReflectionItem::Set {
                    key,
                    value,
                    pinned,
                    keywords,
                },
                crate::memory::ReflectionAction::Note {
                    content,
                    tags,
                    kind,
                } => ReflectionItem::Note {
                    content,
                    tags,
                    kind,
                },
            })
            .collect()
    }

    fn distill_lesson(&self, tag: &str, notes: &str) -> Option<(String, String)> {
        let system = "Ты — консолидатор памяти. Из повторяющихся эпизодов (заметок) \
извлеки урок: активация (1 строка, когда применять) + принцип (развёрнутый вывод, с фактами). \
Верни ТОЛЬКО JSON: {\"activation\":\"...\",\"principle\":\"...\"}";
        let user = format!("Тег: {tag}\nЗаметки-эпизоды:\n{notes}");
        let messages = vec![
            ChatMsg {
                role: "system".into(),
                content: system.to_string(),
            },
            ChatMsg {
                role: "user".into(),
                content: user,
            },
        ];
        let Ok(resp) = self
            .client
            .post(format!(
                "{}/v1/chat/completions",
                self.cfg.base_url.trim_end_matches('/')
            ))
            .json(&ChatRequest {
                model: self.cfg.model.clone(),
                messages,
                tools: None,
                max_tokens: 512,
                temperature: 0.0,
            })
            .send()
        else {
            return None;
        };
        let Ok(parsed) = resp.json::<ChatResp>() else {
            return None;
        };
        let content = parsed
            .choices
            .into_iter()
            .next()
            .and_then(|c| c.message.content)
            .unwrap_or_default();
        let (s, e) = (content.find('{')?, content.rfind('}')?);
        if s >= e {
            return None;
        }
        let v: serde_json::Value = serde_json::from_str(&content[s..=e]).ok()?;
        let activation = v.get("activation")?.as_str()?.to_string();
        let principle = v.get("principle")?.as_str()?.to_string();
        if principle.is_empty() {
            None
        } else {
            Some((activation, principle))
        }
    }

    /// V3.0: LLM distillation of a procedure (activation + steps) from a note cluster.
    fn distill_procedure(&self, tag: &str, notes: &str) -> Option<(String, Vec<String>)> {
        let system = "Ты — консолидатор памяти. Из повторяющихся эпизодов (заметок) \
создай процедуру «как делать правильно»: активация (1 строка, когда применять) + 3-5 шагов. \
Верни ТОЛЬКО JSON без пояснений: {\"activation\":\"...\",\"steps\":[\"...\"]}";
        let user = format!("Тег: {tag}\nЗаметки-эпизоды:\n{notes}");
        let messages = vec![
            ChatMsg {
                role: "system".into(),
                content: system.to_string(),
            },
            ChatMsg {
                role: "user".into(),
                content: user,
            },
        ];
        let Ok(resp) = self
            .client
            .post(format!(
                "{}/v1/chat/completions",
                self.cfg.base_url.trim_end_matches('/')
            ))
            .json(&ChatRequest {
                model: self.cfg.model.clone(),
                messages,
                tools: None,
                max_tokens: 512,
                temperature: 0.0,
            })
            .send()
        else {
            return None;
        };
        let Ok(parsed) = resp.json::<ChatResp>() else {
            return None;
        };
        let content = parsed
            .choices
            .into_iter()
            .next()
            .and_then(|c| c.message.content)
            .unwrap_or_default();
        // cut out the first {...}
        let (s, e) = (content.find('{')?, content.rfind('}')?);
        if s >= e {
            return None;
        }
        let v: serde_json::Value = serde_json::from_str(&content[s..=e]).ok()?;
        let activation = v.get("activation")?.as_str()?.to_string();
        let steps: Vec<String> = v
            .get("steps")?
            .as_array()?
            .iter()
            .filter_map(|x| x.as_str().map(String::from))
            .filter(|x| !x.is_empty())
            .collect();
        if steps.is_empty() {
            None
        } else {
            Some((activation, steps))
        }
    }
}

const SYSTEM_PROMPT: &str = "\
Ты — локально-первый агент ARGUS-OS1. Работаешь по циклу: выбираешь инструменты, \
получаешь сжатые результаты, повторяешь, пока задача не выполнена.
В промпте есть секции: ### cwd (рабочая директория), ### profile (факты о пользователе), \
### lessons (уроки), ### memory-index (последние заметки), ### goal (задача), ### transcript.
Правила:
- Сначала прочитай секции памяти (### profile / ### lessons / ### memory-index) — если ответ \
уже там, отвечай прямо, НЕ вызывая memory.recall.
- Файлы создавай в ### cwd (относительные пути).
- Для задачи «запомни X» вызывай memory.set (короткий факт, pinned если важно) или memory.note \
(свободная заметка, поле kind: event|behavior|knowledge|skill, поле tags).
- file.read — чтение, file.write / shell — опасные, их избегай без необходимости.
ВАЖНО: НЕ печатай вызовы инструментов в тексте ответа (ни \"memory.recall(...)\", ни JSON). \
Если нужен инструмент — используй механизм function calling (tool_calls). Отвечай коротко по-русски.
НИКОГДА не вызывай один и тот же инструмент с одними и теми же аргументами повторно: \
если результат уже получен (например title в HTML) — заверши задачу текстовым ответом.
Когда задача выполнена — НЕ вызывай инструменты и ответь коротко по-русски.";

const REFLECT_PROMPT: &str = "\
Ты — рефлексия памяти локального агента. По окну транскрипта (последние шаги) извлеки \
долговечные факты/наблюдения. Формат — ТОЛЬКО строки, без пояснений:\n\
- SET key=value [pinned=true] [keywords=слова,через,запятую]\n\
- NOTE содержимое заметки [tags=тег1,тег2] [type=event|behavior|knowledge|skill]\n\
Пиши NONE, если ничего ценного нет. Не более 2 строк.";

/// V1.1 recover layer: recognize calls printed as text (memory.note({...}) etc.).
fn recover_text_calls(content: &str) -> Option<Vec<ToolCall>> {
    let known = [
        "memory.set",
        "memory.note",
        "memory.lesson",
        "memory.recall",
        "file.read",
        "file.write",
        "shell",
        "http.get",
        "browser.get",
        "browser.navigate",
        "browser.click",
        "browser.type",
        "browser.snapshot",
        "browser.screenshot",
        "browser.eval",
        "browser.flow",
        "skill.view",
        "skill.run",
        "mcp.tools",
        "mcp.call",
        "web.search",
    ];
    let mut calls = Vec::new();
    for name in known {
        for args in extract_calls_for(content, name) {
            let dangerous = matches!(name, "shell" | "file.write");
            calls.push(ToolCall {
                tool: name.into(),
                args,
                dangerous,
            });
        }
    }
    if !calls.is_empty() {
        return Some(calls);
    }
    // V1.3 fallback: name is misspelled — guess the tool by JSON keys
    for obj in extract_any_json_objects(content) {
        if let Some(tool) = infer_tool_by_keys(&obj) {
            let dangerous = matches!(tool.as_str(), "shell" | "file.write");
            calls.push(ToolCall {
                tool,
                args: obj,
                dangerous,
            });
        }
    }
    if calls.is_empty() {
        None
    } else {
        Some(calls)
    }
}

/// Extracts all `{...}` JSON objects from text.
fn extract_any_json_objects(s: &str) -> Vec<serde_json::Value> {
    let mut out = Vec::new();
    let bytes = s.as_bytes();
    let mut i = 0;
    while i < bytes.len() {
        if bytes[i] == b'{' {
            let mut depth = 0usize;
            let mut j = i;
            let mut in_str = false;
            while j < bytes.len() {
                let b = bytes[j];
                if b == b'"' && (j == 0 || bytes[j - 1] != b'\\') {
                    in_str = !in_str;
                }
                if !in_str {
                    match b {
                        b'{' => depth += 1,
                        b'}' => {
                            depth -= 1;
                            if depth == 0 {
                                if let Ok(v) = serde_json::from_str(&s[i..=j]) {
                                    out.push(v);
                                }
                                break;
                            }
                        }
                        _ => {}
                    }
                }
                j += 1;
            }
        }
        i += 1;
    }
    out
}

/// Guesses the tool by JSON keys (fallback for misspelled names).
fn infer_tool_by_keys(v: &serde_json::Value) -> Option<String> {
    if v.get("url").is_some() {
        Some("http.get".into())
    } else if v.get("query").is_some() {
        Some("memory.recall".into())
    } else if v.get("command").is_some() {
        Some("shell".into())
    } else if v.get("path").is_some() && v.get("content").is_some() {
        Some("file.write".into())
    } else if v.get("path").is_some() {
        Some("file.read".into())
    } else if v.get("content").is_some() {
        Some("memory.note".into())
    } else if v.get("key").is_some() && v.get("value").is_some() {
        Some("memory.set".into())
    } else if v.get("activation").is_some() {
        Some("memory.lesson".into())
    } else {
        None
    }
}

/// Finds `name(...)` in text (object or positional args) and returns the arguments.
fn extract_calls_for(s: &str, name: &str) -> Vec<serde_json::Value> {
    let needle = format!("{name}(");
    let mut out = Vec::new();
    let bytes = s.as_bytes();
    let mut from = 0usize;
    while let Some(rel) = s[from..].find(&needle) {
        let start = from + rel + needle.len();
        let mut i = start;
        while i < bytes.len() && (bytes[i] == b' ' || bytes[i] == b'\n' || bytes[i] == b'\t') {
            i += 1;
        }
        if i < bytes.len() && bytes[i] == b'{' {
            // name({json}) format
            let mut depth = 0usize;
            let mut j = i;
            let mut in_str = false;
            while j < bytes.len() {
                let b = bytes[j];
                if b == b'"' && (j == 0 || bytes[j - 1] != b'\\') {
                    in_str = !in_str;
                }
                if !in_str {
                    match b {
                        b'{' => depth += 1,
                        b'}' => {
                            depth -= 1;
                            if depth == 0 {
                                if let Ok(v) = serde_json::from_str(&s[i..=j]) {
                                    out.push(v);
                                }
                                break;
                            }
                        }
                        _ => {}
                    }
                }
                j += 1;
            }
        } else if i < bytes.len() {
            // name("a", "b", {...}) format — positional arguments
            let open_pos = from + rel + needle.len() - 1; // позиция '(' самого вызова
            if let Some(e) = find_matching_paren(s, open_pos) {
                if let Some(v) = parse_positional(name, &s[open_pos + 1..e]) {
                    out.push(v);
                }
            }
        }
        from = start;
    }
    out
}

/// Finds the matching `)` starting from `open` (bracket/quote balance).
fn find_matching_paren(s: &str, open: usize) -> Option<usize> {
    let bytes = s.as_bytes();
    let mut depth = 0usize;
    let mut in_str = false;
    let mut i = open;
    while i < bytes.len() {
        let b = bytes[i];
        if b == b'"' && (i == 0 || bytes[i - 1] != b'\\') {
            in_str = !in_str;
        }
        if !in_str {
            match b {
                b'(' => depth += 1,
                b')' => {
                    depth -= 1;
                    if depth == 0 {
                        return Some(i);
                    }
                }
                _ => {}
            }
        }
        i += 1;
    }
    None
}

/// Parses positional arguments `("a", "b", {...})` into a JSON object per the tool schema.
fn parse_positional(name: &str, args_src: &str) -> Option<serde_json::Value> {
    // split into top-level elements by commas (respecting strings/brackets)
    let items = split_top_level(args_src);
    let mut vals: Vec<serde_json::Value> = Vec::new();
    for it in items {
        let it = it.trim();
        if it.is_empty() {
            continue;
        }
        if let Ok(v) = serde_json::from_str::<serde_json::Value>(it) {
            vals.push(v);
        }
    }
    if vals.is_empty() {
        return None;
    }
    let sv =
        |i: usize| -> Option<String> { vals.get(i).and_then(|v| v.as_str().map(String::from)) };
    let out = match name {
        "memory.set" => serde_json::json!({
            "key": sv(0).unwrap_or_default(),
            "value": sv(1).unwrap_or_default(),
            "pinned": vals.get(2).and_then(|v| v.get("pinned")).and_then(|p| p.as_bool()).unwrap_or(false),
            "keywords": vals.get(2).and_then(|v| v.get("keywords")).and_then(|k| k.as_array()).cloned().unwrap_or_default()
        }),
        "memory.note" => serde_json::json!({
            "content": sv(0).unwrap_or_default(),
            "tags": vals.get(1).and_then(|v| v.as_array()).cloned().unwrap_or_default(),
            "kind": vals.get(1).and_then(|v| v.get("kind")).and_then(|k| k.as_str()).unwrap_or("knowledge")
        }),
        "memory.recall" => serde_json::json!({ "query": sv(0).unwrap_or_default() }),
        "memory.lesson" => serde_json::json!({
            "activation": sv(0).unwrap_or_default(),
            "principle": sv(1).unwrap_or_default(),
            "tags": vals.get(2).and_then(|v| v.as_array()).cloned().unwrap_or_default()
        }),
        "file.read" => serde_json::json!({ "path": sv(0).unwrap_or_default() }),
        "file.write" => {
            serde_json::json!({ "path": sv(0).unwrap_or_default(), "content": sv(1).unwrap_or_default() })
        }
        "shell" => serde_json::json!({ "command": sv(0).unwrap_or_default() }),
        "http.get" => serde_json::json!({ "url": sv(0).unwrap_or_default() }),
        "browser.get" => serde_json::json!({ "url": sv(0).unwrap_or_default() }),
        "browser.navigate" => serde_json::json!({ "url": sv(0).unwrap_or_default() }),
        "browser.click" => serde_json::json!({ "selector": sv(0).unwrap_or_default() }),
        "browser.type" => {
            serde_json::json!({ "selector": sv(0).unwrap_or_default(), "text": sv(1).unwrap_or_default() })
        }
        "browser.snapshot" => serde_json::json!({}),
        "browser.screenshot" => serde_json::json!({ "path": sv(0).unwrap_or_default() }),
        "browser.eval" => serde_json::json!({ "expression": sv(0).unwrap_or_default() }),
        "browser.flow" => {
            serde_json::json!({ "steps": vals.first().and_then(|v| v.as_array()).cloned().unwrap_or_default() })
        }
        "skill.view" => serde_json::json!({ "name": sv(0).unwrap_or_default() }),
        "mcp.tools" => serde_json::json!({ "server": sv(0).unwrap_or_default() }),
        "mcp.call" => {
            serde_json::json!({ "server": sv(0).unwrap_or_default(), "tool": sv(1).unwrap_or_default(), "args": vals.get(2).cloned().unwrap_or(serde_json::Value::Object(Default::default())) })
        }
        "skill.run" => {
            serde_json::json!({ "name": sv(0).unwrap_or_default(), "script": sv(1).unwrap_or_default(), "args": vals.get(2).and_then(|v| v.as_array()).cloned().unwrap_or_default() })
        }
        "web.search" => serde_json::json!({ "query": sv(0).unwrap_or_default() }),
        _ => return None,
    };
    Some(out)
}

/// Splits an argument string into top-level elements by commas (correct UTF-8).
fn split_top_level(s: &str) -> Vec<String> {
    let mut out = Vec::new();
    let mut depth = 0i32;
    let mut in_str = false;
    let mut prev_bs = false; // предыдущий символ — обратный слэш (escape)
    let mut cur = String::new();
    for c in s.chars() {
        if c == '"' && !prev_bs {
            in_str = !in_str;
        }
        if !in_str {
            match c {
                '(' | '{' | '[' => depth += 1,
                ')' | '}' | ']' => depth -= 1,
                ',' if depth == 0 => {
                    out.push(std::mem::take(&mut cur));
                    continue;
                }
                _ => {}
            }
        }
        cur.push(c);
        prev_bs = c == '\\';
    }
    out.push(cur);
    out
}

fn build_tools() -> Vec<ToolDef> {
    let s = |name: &str, desc: &str, params: serde_json::Value| ToolDef {
        ty: "function".into(),
        function: FnDef {
            name: name.into(),
            description: desc.into(),
            parameters: params,
        },
    };
    vec![
        s("memory.set", "Сохранить профиль-факт (key/value). keywords — слова, при которых факт вспоминать; pinned=true — всегда.",
          serde_json::json!({
            "type":"object",
            "properties":{
                "key":{"type":"string"},
                "value":{"type":"string"},
                "pinned":{"type":"boolean","default":false},
                "keywords":{"type":"array","items":{"type":"string"}}
            },
            "required":["key","value"]
          })),
        s("memory.note", "Сохранить заметку. kind: event|behavior|knowledge|skill; tags — массив тегов.",
          serde_json::json!({
            "type":"object",
            "properties":{
                "content":{"type":"string"},
                "tags":{"type":"array","items":{"type":"string"}},
                "kind":{"type":"string","enum":["event","behavior","knowledge","skill"],"default":"knowledge"}
            },
            "required":["content"]
          })),
        s("memory.lesson", "Сохранить урок (активация + принцип + теги) из повторяющегося эпизода.",
          serde_json::json!({
            "type":"object",
            "properties":{
                "activation":{"type":"string"},
                "principle":{"type":"string"},
                "tags":{"type":"array","items":{"type":"string"}}
            },
            "required":["activation","principle"]
          })),
        s("memory.recall", "Найти заметки по запросу (подстрока по тексту/тегам).",
          serde_json::json!({
            "type":"object",
            "properties":{"query":{"type":"string"}},
            "required":["query"]
          })),
        s("file.read", "Прочитать файл (сжато, до 2000 символов). path — абсолютный или относительно cwd.",
          serde_json::json!({
            "type":"object",
            "properties":{"path":{"type":"string"}},
            "required":["path"]
          })),
        s("file.write", "Записать файл (ОПАСНО — требует одобрения). path, content.",
          serde_json::json!({
            "type":"object",
            "properties":{"path":{"type":"string"},"content":{"type":"string"}},
            "required":["path","content"]
          })),
        s("shell", "Выполнить shell-команду (ОПАСНО — требует одобрения). command.",
          serde_json::json!({
            "type":"object",
            "properties":{"command":{"type":"string"}},
            "required":["command"]
          })),
        s("http.get", "Загрузить веб-страницу по URL (SSRF-guarded: private/loopback запрещены). http/https только.",
          serde_json::json!({
            "type":"object",
            "properties":{"url":{"type":"string"}},
            "required":["url"]
          })),
        s("browser.get", "Открыть страницу в реальном браузере (headless Chrome, JS-рендер). url — http(s).",
          serde_json::json!({
            "type":"object",
            "properties":{"url":{"type":"string"}},
            "required":["url"]
          })),
        s("browser.navigate", "Открыть URL в CDP-браузере (новая вкладка). url — http(s).",
          serde_json::json!({
            "type":"object",
            "properties":{"url":{"type":"string"}},
            "required":["url"]
          })),
        s("browser.click", "Клик по элементу по CSS-селектору в браузере. selector.",
          serde_json::json!({
            "type":"object",
            "properties":{"selector":{"type":"string"}},
            "required":["selector"]
          })),
        s("browser.type", "Ввести текст в поле ввода по CSS-селектору. selector, text.",
          serde_json::json!({
            "type":"object",
            "properties":{"selector":{"type":"string"},"text":{"type":"string"}},
            "required":["selector","text"]
          })),
        s("browser.screenshot", "Снять скриншот страницы в PNG-файл. path — куда сохранить.", serde_json::json!({"type":"object","properties":{"path":{"type":"string"}},"required":["path"]})),
        s("browser.snapshot", "Снять состояние страницы: title + видимый текст.",
          serde_json::json!({"type":"object","properties":{}})),
        s("browser.eval", "Выполнить произвольный JS-код на странице (ВНИМАНИЕ: может менять страницу). expression.",
          serde_json::json!({
            "type":"object",
            "properties":{"expression":{"type":"string"}},
            "required":["expression"]
          })),
        s("browser.flow", "Выполнить сценарий из шагов [{op:navigate|click|type|eval|snapshot, url?, selector?, text?, expression?}] и вернуть итоговый снимок.",
          serde_json::json!({
            "type":"object",
            "properties":{
                "steps":{"type":"array","items":{"type":"object"}}
            },
            "required":["steps"]
          })),
        s("skill.view", "Показать тело скилла по name (описание + инструкция).",
          serde_json::json!({
            "type":"object",
            "properties":{"name":{"type":"string"}},
            "required":["name"]
          })),
        s("mcp.tools", "Список инструментов MCP-сервера (server — имя из mcp_servers.json).", serde_json::json!({"type":"object","properties":{"server":{"type":"string"}},"required":["server"]})),
        s("mcp.call", "Вызвать инструмент MCP-сервера. server, tool, args (JSON-объект).", serde_json::json!({"type":"object","properties":{"server":{"type":"string"},"tool":{"type":"string"},"args":{"type":"object"}},"required":["server","tool"]})),
        s("skill.run", "Выполнить скрипт скилла (ОПАСНО — одобрение). name, script (из requires_scripts), args.",
          serde_json::json!({
            "type":"object",
            "properties":{
                "name":{"type":"string"},
                "script":{"type":"string"},
                "args":{"type":"array","items":{"type":"string"}}
            },
            "required":["name","script"]
          })),
        s("web.search", "Поиск в вебе (DuckDuckGo, без ключа). query — поисковый запрос.",
          serde_json::json!({
            "type":"object",
            "properties":{"query":{"type":"string"}},
            "required":["query"]
          })),
    ]
}

/// Stub model for offline tests.
pub struct StubModel;

impl Model for StubModel {
    fn decide(&self, prompt: &str) -> AgentDecision {
        if prompt.contains("[step 1]") {
            return AgentDecision::Reply("стаб: готово".into());
        }
        if prompt.contains("remember") {
            AgentDecision::Tools(vec![ToolCall {
                tool: "memory.note".into(),
                args: serde_json::json!({
                    "content": "пример заметки из стаб-модели",
                    "tags": ["demo"],
                    "kind": "knowledge"
                }),
                dangerous: false,
            }])
        } else {
            AgentDecision::Reply("стаб: нет действий".into())
        }
    }
    fn compress(&self, results: &[ToolResult]) -> String {
        results
            .iter()
            .map(|r| format!("{}: {}", r.tool, r.summary))
            .collect::<Vec<_>>()
            .join("; ")
    }
    fn reflect(&self, _window: &str) -> Vec<ReflectionItem> {
        Vec::new()
    }
    fn distill_procedure(&self, _tag: &str, _notes: &str) -> Option<(String, Vec<String>)> {
        None
    }
    fn distill_lesson(&self, _tag: &str, _notes: &str) -> Option<(String, String)> {
        None
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn recover_object_format() {
        let calls = recover_text_calls(
            r#"посмотри memory.note({"content":"x"}) и file.read({"path":"/a"})"#,
        )
        .unwrap();
        assert_eq!(calls.len(), 2);
        assert_eq!(calls[0].tool, "memory.note");
        assert_eq!(calls[1].tool, "file.read");
    }

    #[test]
    fn recover_positional_format() {
        let calls =
            recover_text_calls(r#"сделай memory.note("текст", {"tags":["a"]}) и shell("ls -la")"#)
                .unwrap_or_default();
        println!("calls: {:?}", calls);
        let note = calls.iter().find(|c| c.tool == "memory.note").unwrap();
        assert_eq!(note.args["content"], "текст");
        let sh = calls.iter().find(|c| c.tool == "shell").unwrap();
        assert_eq!(sh.args["command"], "ls -la");
        assert!(sh.dangerous);
    }

    #[test]
    fn recover_none_on_plain_text() {
        assert!(recover_text_calls("просто ответ по-русски").is_none());
    }

    #[test]
    fn recover_fuzzy_typo() {
        // name misspelled (bral.get) — fallback by url key
        let calls = recover_text_calls(r#"bral.get({"url": "https://example.com"})"#).unwrap();
        assert_eq!(calls[0].tool, "http.get");
        assert_eq!(calls[0].args["url"], "https://example.com");
    }

    #[test]
    fn referential_heuristic() {
        assert!(is_referential("и про это"));
        assert!(is_referential("а что там?"));
        assert!(!is_referential("прочитай файл config.json и скажи размер"));
    }

    #[test]
    fn reflection_parser() {
        let acts = crate::memory::parse_reflection(
            "SET name=Jaba [pinned=true]\nNOTE лазерной абляции нет [tags=argus,method] [type=knowledge]\nNONE",
        );
        assert_eq!(acts.len(), 2);
        match &acts[0] {
            crate::memory::ReflectionAction::Set { key, pinned, .. } => {
                assert_eq!(key, "name");
                assert!(*pinned);
            }
            _ => panic!("ожидался SET"),
        }
        match &acts[1] {
            crate::memory::ReflectionAction::Note { tags, kind, .. } => {
                assert!(tags.contains(&"argus".to_string()));
                assert_eq!(*kind, NoteKind::Knowledge);
            }
            _ => panic!("ожидался NOTE"),
        }
    }

    #[test]
    fn ssrf_guard() {
        assert!(is_safe_url("https://example.com/page"));
        assert!(is_safe_url("http://8.8.8.8/"));
        assert!(!is_safe_url("http://localhost/"));
        assert!(!is_safe_url("http://127.0.0.1:8080/v1"));
        assert!(!is_safe_url("http://192.168.1.1/x"));
        assert!(!is_safe_url("http://10.0.0.1/"));
        assert!(!is_safe_url("http://172.16.0.1/"));
        assert!(!is_safe_url("ftp://example.com"));
        assert!(!is_safe_url("file:///etc/passwd"));
    }
}
