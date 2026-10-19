//! Plugin hooks (V2.3): external commands invoked at agent-loop points.
//! Events: before_step / after_step / on_done / on_error.
//! Hooks are fire-and-forget (they do not block the loop). Context via env: ARGUS_GOAL,
//! ARGUS_STEP, ARGUS_SUMMARY, ARGUS_TOOLS.
use serde::{Deserialize, Serialize};
use std::path::Path;

#[derive(Serialize, Deserialize, Clone, Debug, Default)]
#[serde(default)]
pub struct Plugin {
    pub id: u64,
    pub event: String,
    pub command: String,
    /// V2.7: for event="timer" — run period (seconds)
    pub interval_sec: Option<u64>,
    /// V2.8: last timer-fire time (persisted in plugins.json)
    pub last_fire: Option<u64>,
}

pub const EVENTS: &[&str] = &["before_step", "after_step", "on_done", "on_error", "timer"];

pub fn load(state_dir: &Path) -> Vec<Plugin> {
    std::fs::read_to_string(state_dir.join("plugins.json"))
        .ok()
        .and_then(|s| serde_json::from_str(&s).ok())
        .unwrap_or_default()
}

fn save(state_dir: &Path, plugins: &[Plugin]) {
    if let Ok(s) = serde_json::to_string_pretty(plugins) {
        let _ = std::fs::write(state_dir.join("plugins.json"), s);
    }
}

pub fn add(
    state_dir: &Path,
    event: &str,
    command: &str,
    interval: Option<u64>,
) -> Result<u64, String> {
    if !EVENTS.contains(&event) {
        return Err(format!("событие '{event}' не из {:?}", EVENTS));
    }
    if event == "timer" && interval.is_none() {
        return Err("для события timer требуется --interval <сек>".into());
    }
    if command.trim().is_empty() {
        return Err("пустая команда".into());
    }
    let mut plugins = load(state_dir);
    let id = plugins.iter().map(|p| p.id).max().unwrap_or(0) + 1;
    plugins.push(Plugin {
        id,
        event: event.to_string(),
        command: command.to_string(),
        interval_sec: interval,
        last_fire: None,
    });
    save(state_dir, &plugins);
    Ok(id)
}

pub fn remove(state_dir: &Path, id: u64) -> Result<(), String> {
    let mut plugins = load(state_dir);
    let before = plugins.len();
    plugins.retain(|p| p.id != id);
    if plugins.len() == before {
        return Err(format!("плагин #{id} не найден"));
    }
    save(state_dir, &plugins);
    Ok(())
}

/// Runs the event hooks from the given plugin slice. Does not block the loop (spawn).
pub fn run_plugins(plugins: &[Plugin], event: &str, env: &[(&str, String)]) {
    for p in plugins.iter().filter(|p| p.event == event) {
        run_one(p, env);
    }
}

/// V2.7: timer hooks (event="timer") — run at most once per interval_sec.
/// Last-fire state lives in `last_fires` (in the loop's memory).
pub fn run_timers(plugins: &mut [Plugin], now: u64, env: &[(&str, String)]) {
    for p in plugins.iter_mut().filter(|p| p.event == "timer") {
        let Some(interval) = p.interval_sec else {
            continue;
        };
        if interval == 0 {
            continue;
        }
        let last = p.last_fire.unwrap_or(0);
        if now.saturating_sub(last) >= interval {
            run_one(p, env);
            p.last_fire = Some(now);
        }
    }
}

/// V2.8: public save (to persist last_fire after run).
pub fn save_pub(state_dir: &Path, plugins: &[Plugin]) {
    save(state_dir, plugins);
}

fn run_one(p: &Plugin, env: &[(&str, String)]) {
    let mut cmd = std::process::Command::new("sh");
    cmd.arg("-c").arg(&p.command);
    for (k, v) in env {
        cmd.env(k, v);
    }
    let _ = cmd.spawn();
}

pub fn now_sec() -> u64 {
    std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map(|d| d.as_secs())
        .unwrap_or(0)
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::path::PathBuf;

    #[test]
    fn timer_hook_respects_interval() {
        let dir = PathBuf::from("/tmp/argus-plug-test");
        let _ = std::fs::remove_dir_all(&dir);
        std::fs::create_dir_all(&dir).ok();
        let id = add(
            &dir,
            "timer",
            "echo t >> /tmp/argus-plug-test/t.log",
            Some(100),
        )
        .unwrap();
        let mut plugins = load(&dir);
        // first tick fires (last_fire=0)
        run_timers(&mut plugins, 1000, &[]);
        assert_eq!(plugins[0].last_fire, Some(1000));
        // repeat tick within the interval — does not fire
        run_timers(&mut plugins, 1050, &[]);
        assert_eq!(plugins[0].last_fire, Some(1000));
        // beyond the interval — fires
        run_timers(&mut plugins, 1150, &[]);
        assert_eq!(plugins[0].last_fire, Some(1150));
        let _ = id;
        let _ = std::fs::remove_dir_all(&dir);
    }
}
