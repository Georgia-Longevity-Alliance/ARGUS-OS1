//! Plugin skills (V1.5): Markdown playbooks (Atomic/pi SKILL.md format).
//! Progressive loading: only name+description go into the prompt; body via skill.view.
//! Scripts run only from requires_scripts and with approval (dangerous).
use serde::Deserialize;
use std::path::{Path, PathBuf};

#[derive(Debug, Clone)]
pub struct Skill {
    pub name: String,
    pub description: String,
    pub version: String,
    pub requires_tools: Vec<String>,
    pub requires_scripts: Vec<String>,
    pub dangerous: bool,
    /// SKILL.md body (after frontmatter) — loaded via skill.view
    pub body: String,
    /// absolute path to the skill folder (for scripts/)
    pub dir: PathBuf,
}

/// Loads all skills from <stateDir>/skills/<name>/SKILL.md.
pub fn load_skills(state_dir: &Path) -> Vec<Skill> {
    let skills_dir = state_dir.join("skills");
    let mut out = Vec::new();
    let Ok(entries) = std::fs::read_dir(&skills_dir) else {
        return out;
    };
    for e in entries.flatten() {
        let p = e.path();
        if !p.is_dir() {
            continue;
        }
        let sk = p.join("SKILL.md");
        if let Some(s) = load_skill(&sk) {
            out.push(s);
        }
    }
    out
}

fn load_skill(skill_md: &Path) -> Option<Skill> {
    let text = std::fs::read_to_string(skill_md).ok()?;
    if !text.starts_with("---") {
        return None;
    }
    let rest = &text[3..];
    let end = rest.find("\n---")?;
    let front = &rest[..end];
    let body = rest[end + 4..].trim_start().to_string();
    let dir = skill_md.parent()?.to_path_buf();

    let get = |key: &str| -> Option<String> {
        front.lines().find_map(|l| {
            l.trim()
                .strip_prefix(key)?
                .trim()
                .strip_prefix(':')
                .map(|v| v.trim().trim_matches('"').to_string())
        })
    };
    let list = |key: &str| -> Vec<String> {
        let Some(v) = get(key) else { return Vec::new() };
        v.trim_start_matches('[')
            .trim_end_matches(']')
            .split(',')
            .map(|s| s.trim().trim_matches('"').to_string())
            .filter(|s| !s.is_empty())
            .collect()
    };
    Some(Skill {
        name: get("name")?,
        description: get("description").unwrap_or_default(),
        version: get("version").unwrap_or_else(|| "0.0.1".into()),
        requires_tools: list("requires_tools"),
        requires_scripts: list("requires_scripts"),
        dangerous: get("dangerous").map(|v| v == "true").unwrap_or(false),
        body,
        dir,
    })
}

/// Skill search by description/name (simple lexical: all words must appear).
pub fn find_skill<'a>(skills: &'a [Skill], query: &str) -> Option<&'a Skill> {
    let q = query.to_lowercase();
    let words: Vec<&str> = q.split_whitespace().collect();
    skills.iter().find(|s| {
        let hay = format!("{} {}", s.name.to_lowercase(), s.description.to_lowercase());
        words.iter().all(|w| hay.contains(w))
    })
}

/// Prompt index: name+description of all skills (stable prefix, KV cache).
pub fn skills_index(skills: &[Skill]) -> String {
    if skills.is_empty() {
        return String::new();
    }
    let mut out = String::from("### skills\n");
    for s in skills {
        out.push_str(&format!("- {}: {}\n", s.name, s.description));
    }
    out
}

/// Runs a skill script: only from requires_scripts; dangerous=true always.
pub fn run_script(skill: &Skill, script: &str, args: &[String]) -> Result<String, String> {
    if !skill.requires_scripts.iter().any(|r| r == script) {
        return Err(format!(
            "скрипт '{script}' не в requires_scripts скилла {}",
            skill.name
        ));
    }
    let path = skill.dir.join("scripts").join(script);
    if !path.exists() {
        return Err(format!("скрипт не найден: {}", path.display()));
    }
    let mut cmd = std::process::Command::new("sh");
    cmd.arg(&path).args(args);
    let out = cmd.output().map_err(|e| format!("запуск: {e}"))?;
    let mut s = String::from_utf8_lossy(&out.stdout).to_string();
    if !out.stderr.is_empty() {
        s.push_str(&format!(
            "\n[stderr] {}",
            String::from_utf8_lossy(&out.stderr)
        ));
    }
    Ok(format!(
        "exit={}:\n{}",
        out.status.code().unwrap_or(-1),
        s.chars().take(1200).collect::<String>()
    ))
}

/// Built-in skill registry (V1.6): (name, description). Installation = SKILL.md copy.
pub const REGISTRY: &[(&str, &str)] = &[
    ("docker", "Управление Docker: образы, контейнеры, логи"),
    ("pdf", "Извлечение текста из PDF локально (pdftotext)"),
    (
        "obsidian",
        "Чтение/поиск в Obsidian-ваулте (OBSIDIAN_VAULT_PATH)",
    ),
    ("notion", "Чтение и заметки в Notion (интеграция)"),
    ("github", "Создание issue/PR, комментарии (токен)"),
    ("pandoc", "Конвертация документов (markdown→docx/pdf)"),
    ("xlsx", "Чтение/анализ Excel-файлов (xlsx2csv)"),
    ("ffmpeg", "Обработка видео/аудио (ffmpeg)"),
    ("imagemagick", "Конвертация/обработка изображений (convert)"),
    ("currency", "Актуальные курсы валют (API)"),
    // V1.8: browser recipes (body = ready browser.flow template)
    (
        "web-research",
        "Открыть страницу и собрать текст (browser.flow: navigate+snapshot)",
    ),
    ("form-fill", "Заполнить форму: navigate+type+click+snapshot"),
    (
        "login-flow",
        "Логин: navigate+type username+type password+click+snapshot",
    ),
];

/// Browser recipes (V1.8): ready flow templates as skills.
pub const RECIPES: &[(&str, &str)] = &[
    (
        "web-research",
        "Открыть страницу и собрать текст (browser.flow: navigate+snapshot)",
    ),
    (
        "form-fill",
        "Заполнить форму: navigate+type по селекторам+click submit+snapshot",
    ),
    (
        "login-flow",
        "Логин: navigate+type username+type password+click+snapshot",
    ),
    (
        "search-query",
        "Поиск на сайте: navigate к поиску, type запрос, click, snapshot",
    ),
    (
        "collect-links",
        "Собрать ссылки: navigate + eval document.querySelectorAll('a')",
    ),
    (
        "extract-table",
        "Извлечь таблицу: navigate + eval innerText таблиц",
    ),
    (
        "download-file",
        "Скачать файл по ссылке: navigate + eval href + browser.get",
    ),
    (
        "pagination",
        "Пройти все страницы: navigate, клик «next», собирать снимки",
    ),
    (
        "check-status",
        "Проверить доступность: browser.navigate + snapshot",
    ),
];

/// Registry search (all words must appear in the description).
pub fn search_registry(query: &str) -> Vec<(&'static str, &'static str)> {
    let q = query.to_lowercase();
    let words: Vec<&str> = q.split_whitespace().collect();
    REGISTRY
        .iter()
        .filter(|(n, d)| {
            let hay = format!("{n} {d}").to_lowercase();
            words.iter().all(|w| hay.contains(w))
        })
        .copied()
        .collect()
}

/// Installs a skill from the registry into <stateDir>/skills/<name>/SKILL.md.
pub fn install_from_registry(state_dir: &Path, name: &str) -> Result<usize, String> {
    let entry = REGISTRY
        .iter()
        .find(|(n, _)| n.eq_ignore_ascii_case(name))
        .ok_or_else(|| format!("в реестре нет скилла '{name}' (см. skill search)"))?;
    let dir = state_dir.join("skills").join(entry.0);
    if dir.join("SKILL.md").exists() {
        return Err(format!("скилл '{}' уже установлен", entry.0));
    }
    std::fs::create_dir_all(&dir).map_err(|e| format!("создать папку: {e}"))?;
    // V1.8: browser recipe — body with a ready browser.flow template
    let recipe_body = RECIPES
        .iter()
        .find(|(n, _)| n.eq_ignore_ascii_case(name))
        .map(|(_, desc)| {
            format!(
                "Инструкция: {desc}\n\nИспользуй browser.flow со steps:\n\
                 {{ \"steps\": [{{\"op\":\"navigate\",\"url\":\"URL\"}}, \
                 {{\"op\":\"type\",\"selector\":\"SEL\",\"text\":\"TEXT\"}}, \
                 {{\"op\":\"click\",\"selector\":\"SUBMIT_SEL\"}}, \
                 {{\"op\":\"snapshot\"}}] }}\n"
            )
        })
        .unwrap_or_else(|| format!("Инструкция: {}\n", entry.1));
    let md = format!(
        "---\nname: {}\ndescription: \"{}\"\nversion: 0.1.0\nrequires_tools: [browser.flow]\nrequires_scripts: []\ndangerous: false\n---\n\n{recipe_body}",
        entry.0, entry.1
    );
    std::fs::write(dir.join("SKILL.md"), md).map_err(|e| format!("записать: {e}"))?;
    Ok(1)
}

/// V3.6: import skills from pi (~/.pi/agent/skills/<name>/SKILL.md).
pub fn import_from_pi(state_dir: &Path, pi_dir: &Path) -> usize {
    let pi_skills = pi_dir.join("skills");
    let Ok(entries) = std::fs::read_dir(&pi_skills) else {
        return 0;
    };
    let mut count = 0usize;
    for e in entries.flatten() {
        let p = e.path();
        let sk = if p.is_dir() { p.join("SKILL.md") } else { p };
        if sk.extension().map(|x| x == "md").unwrap_or(false) {
            if let Ok(text) = std::fs::read_to_string(&sk) {
                if text.starts_with("---") {
                    if let Some(skill) = load_skill(&sk) {
                        let dest = state_dir.join("skills").join(&skill.name);
                        let _ = std::fs::create_dir_all(&dest);
                        let _ = std::fs::write(dest.join("SKILL.md"), text);
                        count += 1;
                    }
                }
            }
        }
    }
    count
}

/// Lists taps (owner/repo) from <stateDir>/taps.json.
pub fn load_taps(state_dir: &Path) -> Vec<String> {
    let p = state_dir.join("taps.json");
    std::fs::read_to_string(p)
        .ok()
        .and_then(|s| serde_json::from_str::<Vec<String>>(&s).ok())
        .unwrap_or_default()
}

fn save_taps(state_dir: &Path, taps: &[String]) {
    if let Ok(s) = serde_json::to_string_pretty(taps) {
        let _ = std::fs::write(state_dir.join("taps.json"), s);
    }
}

pub fn tap_add(state_dir: &Path, spec: &str) -> Result<(), String> {
    if !spec.contains('/') {
        return Err("формат: owner/repo".into());
    }
    let mut taps = load_taps(state_dir);
    if taps.iter().any(|t| t.eq_ignore_ascii_case(spec)) {
        return Err(format!("тап '{spec}' уже есть"));
    }
    taps.push(spec.to_string());
    save_taps(state_dir, &taps);
    Ok(())
}

pub fn tap_remove(state_dir: &Path, spec: &str) -> Result<(), String> {
    let mut taps = load_taps(state_dir);
    let before = taps.len();
    taps.retain(|t| !t.eq_ignore_ascii_case(spec));
    if taps.len() == before {
        return Err(format!("тап '{spec}' не найден"));
    }
    save_taps(state_dir, &taps);
    Ok(())
}

/// Installs a skill from a GitHub tap: spec = owner/repo[/subpath].
/// Downloads SKILL.md from raw.githubusercontent.com (main), saves under the frontmatter name.
pub fn install_from_github(state_dir: &Path, spec: &str) -> Result<String, String> {
    let mut parts: Vec<&str> = spec.split('/').collect();
    if parts.len() < 2 {
        return Err("формат: owner/repo[/path]".into());
    }
    let owner = parts.remove(0);
    let repo = parts.remove(0);
    let sub = parts.join("/");
    let base = if sub.is_empty() {
        format!("{owner}/{repo}/main")
    } else {
        format!("{owner}/{repo}/main/{sub}")
    };
    let url = format!("https://raw.githubusercontent.com/{base}/SKILL.md");
    let body = reqwest::blocking::get(&url)
        .map_err(|e| format!("скачать {url}: {e}"))?
        .error_for_status()
        .map_err(|e| format!("HTTP {e}"))?
        .text()
        .map_err(|e| format!("чтение: {e}"))?;
    let skill =
        load_skill_from_str(&body).ok_or("не удалось распарсить SKILL.md (нет frontmatter)")?;
    let dir = state_dir.join("skills").join(&skill.name);
    std::fs::create_dir_all(&dir).map_err(|e| format!("создать папку: {e}"))?;
    std::fs::write(dir.join("SKILL.md"), body).map_err(|e| format!("записать: {e}"))?;
    Ok(skill.name)
}

fn load_skill_from_str(text: &str) -> Option<Skill> {
    if !text.starts_with("---") {
        return None;
    }
    let rest = &text[3..];
    let end = rest.find("\n---")?;
    let front = &rest[..end];
    let body = rest[end + 4..].trim_start().to_string();
    let dir = std::path::PathBuf::from(".");
    let get = |key: &str| -> Option<String> {
        front.lines().find_map(|l| {
            l.trim()
                .strip_prefix(key)?
                .trim()
                .strip_prefix(':')
                .map(|v| v.trim().trim_matches('"').to_string())
        })
    };
    let list = |key: &str| -> Vec<String> {
        let Some(v) = get(key) else { return Vec::new() };
        v.trim_start_matches('[')
            .trim_end_matches(']')
            .split(',')
            .map(|s| s.trim().trim_matches('"').to_string())
            .filter(|s| !s.is_empty())
            .collect()
    };
    Some(Skill {
        name: get("name")?,
        description: get("description").unwrap_or_default(),
        version: get("version").unwrap_or_else(|| "0.0.1".into()),
        requires_tools: list("requires_tools"),
        requires_scripts: list("requires_scripts"),
        dangerous: get("dangerous").map(|v| v == "true").unwrap_or(false),
        body,
        dir,
    })
}

#[derive(Deserialize, Debug)]
pub struct SkillCall {
    pub name: String,
    #[serde(default)]
    pub script: Option<String>,
    #[serde(default)]
    pub args: Vec<String>,
}

/// Hub server (V1.8, ClawHub-style): GET /skills (JSON) and /skills/<name> (SKILL.md).
pub fn serve(state_dir: &Path, port: u16) -> Result<(), String> {
    use std::io::{Read, Write};
    use std::net::TcpListener;

    let listener = TcpListener::bind(("127.0.0.1", port)).map_err(|e| format!("bind: {e}"))?;
    println!("🟢 skill hub на http://127.0.0.1:{port} (Ctrl+C для выхода)");
    for stream in listener.incoming() {
        let Ok(mut stream) = stream else { continue };
        let mut buf = [0u8; 8192];
        let n = stream.read(&mut buf).unwrap_or(0);
        let req = String::from_utf8_lossy(&buf[..n]).to_string();
        let req_line = req.lines().next().unwrap_or("").to_string();
        let mut parts = req_line.split_whitespace();
        let method = parts.next().unwrap_or("GET").to_string();
        let path = parts.next().unwrap_or("/").to_string();
        let skills = load_skills(state_dir);
        let (status, body, ctype) = if method == "POST" || method == "PUT" {
            // V3.3: auth for publishing (ARGUS_HUB_TOKEN); GET stays public
            let need = std::env::var("ARGUS_HUB_TOKEN").unwrap_or_default();
            if !need.is_empty() {
                let header = req
                    .lines()
                    .find(|l| l.to_lowercase().starts_with("authorization:"))
                    .unwrap_or("");
                let tok = header.split_whitespace().nth(2).unwrap_or("").trim();
                if tok != need.trim() {
                    (
                        "401 Unauthorized",
                        "bad or missing Bearer token".into(),
                        "text/plain",
                    )
                } else {
                    serve_publish(state_dir, &req, &path)
                }
            } else {
                serve_publish(state_dir, &req, &path)
            }
        } else if path == "/tasks" {
            // V3.4: task dashboard — JSON task list from tasks.json (+due)
            let now = std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .map(|d| d.as_secs())
                .unwrap_or(0);
            let tasks_raw = std::fs::read_to_string(state_dir.join("tasks.json"))
                .unwrap_or_else(|_| "[]".into());
            let tasks: serde_json::Value =
                serde_json::from_str(&tasks_raw).unwrap_or(serde_json::Value::Array(vec![]));
            let dashboard = serde_json::json!({
                "now": now,
                "tasks": tasks.as_array().cloned().unwrap_or_default(),
                "due": tasks.as_array().map(|a| a.iter().filter(|t| t.get("next_due").and_then(|d| d.as_u64()).unwrap_or(0) <= now).count()).unwrap_or(0)
            });
            ("200 OK", dashboard.to_string(), "application/json")
        } else if path == "/skills" || path.starts_with("/skills?q=") {
            // V3.5: hub catalog — search by ?q= (name/description)
            let q = path.strip_prefix("/skills?q=").unwrap_or("").to_lowercase();
            let filtered: Vec<_> = skills
                .iter()
                .filter(|s| {
                    q.is_empty()
                        || s.name.to_lowercase().contains(&q)
                        || s.description.to_lowercase().contains(&q)
                })
                .collect();
            let list: Vec<serde_json::Value> = filtered
                .iter()
                .map(|s| {
                    serde_json::json!({
                        "name": s.name,
                        "description": s.description,
                        "version": s.version,
                        "dangerous": s.dangerous
                    })
                })
                .collect();
            (
                "200 OK",
                serde_json::to_string_pretty(&list).unwrap_or_default(),
                "application/json",
            )
        } else if let Some(name) = path
            .strip_prefix("/skills/")
            .and_then(|n| n.strip_suffix("/version"))
        {
            // V3.5: skill version
            match skills.iter().find(|s| s.name == name) {
                Some(s) => (
                    "200 OK",
                    serde_json::json!({"name": s.name, "version": s.version}).to_string(),
                    "application/json",
                ),
                None => ("404 Not Found", "skill not found".into(), "text/plain"),
            }
        } else if let Some(name) = path.strip_prefix("/skills/") {
            match skills.iter().find(|s| s.name == name) {
                Some(s) => (
                    "200 OK",
                    format!("# {}\n\n{}", s.name, s.body),
                    "text/markdown",
                ),
                None => ("404 Not Found", "skill not found".into(), "text/plain"),
            }
        } else {
            (
                "404 Not Found",
                "use /skills or /skills/<name>".into(),
                "text/plain",
            )
        };
        let resp = format!(
            "HTTP/1.1 {status}\r\nContent-Type: {ctype}\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{body}",
            body.len()
        );
        let _ = stream.write_all(resp.as_bytes());
    }
    Ok(())
}

/// V3.3: POST /skills/<name> handler (after token check).
fn serve_publish(state_dir: &Path, req: &str, path: &str) -> (&'static str, String, &'static str) {
    if let Some(name) = path.trim_start_matches('/').strip_prefix("skills/") {
        let name = name.trim_end_matches('/').to_string();
        let body_start = req.find("\r\n\r\n").map(|i| i + 4).unwrap_or(0);
        let md = &req[body_start..];
        if md.trim().is_empty() || name.is_empty() {
            ("400 Bad Request", "empty body".into(), "text/plain")
        } else {
            let dir = state_dir.join("skills").join(&name);
            let _ = std::fs::create_dir_all(&dir);
            match std::fs::write(dir.join("SKILL.md"), md) {
                Ok(()) => ("200 OK", format!("skill '{name}' published"), "text/plain"),
                Err(e) => ("500 Internal Server Error", e.to_string(), "text/plain"),
            }
        }
    } else {
        (
            "404 Not Found",
            "use POST /skills/<name>".into(),
            "text/plain",
        )
    }
}

/// Client: publish a skill to the hub (POST /skills/<name>).
pub fn push_skill(
    remote: &str,
    state_dir: &Path,
    name: &str,
    token: &str,
) -> Result<String, String> {
    let skills = load_skills(state_dir);
    let skill = skills
        .iter()
        .find(|s| s.name == name)
        .ok_or_else(|| format!("скилл '{name}' не установлен"))?;
    let md =
        std::fs::read_to_string(skill.dir.join("SKILL.md")).map_err(|e| format!("читать: {e}"))?;
    let url = format!("{}/skills/{}", remote.trim_end_matches('/'), name);
    let mut req_b = reqwest::blocking::Client::new().post(&url).body(md);
    if !token.is_empty() {
        req_b = req_b.header("Authorization", format!("Bearer {token}"));
    }
    let resp = req_b.send().map_err(|e| format!("push {url}: {e}"))?;
    let status = resp.status();
    let body = resp.text().unwrap_or_default();
    if status.is_success() {
        Ok(format!("✅ '{name}' → {url} ({status})"))
    } else {
        Err(format!("push: {status} {body}"))
    }
}
