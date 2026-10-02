# ARGUS-OS1 — User Documentation (V1.9)

Local-first AI agent core. This is the full user guide; see [README.md](README.md)
for the quick start and [GRANT_KIT.md](GRANT_KIT.md) for the open-source/grant
package.

## Installation & build

Requirements: Rust toolchain, an OpenAI-compatible LLM server (default: Ollama on
`127.0.0.1:11434`; works with LM Studio `127.0.0.1:1234`, llama-server, cloud).

```bash
cd Services
cargo build --release --bin argus-agent
cargo test -p argus-pre --lib                 # 9 unit tests
# optional: real-browser integration tests (needs google-chrome)
cargo test -p argus-pre --lib -- --ignored
```

## CLI reference

| Command | What it does |
|---|---|
| `init` | create `~/.argus-agent/` memory + starter skills (docker/pdf/obsidian) |
| `run "goal" [--url --model --mode --yes --cwd]` | one-shot agent loop |
| `memory add "text" --kind X` | save a note (event\|behavior\|knowledge\|skill) |
| `memory recall "query" [--k N] [--vector local\|ollama]` | hybrid recall (substring + vector similarity) |
| `memory vote / procedures / links / link <a> <b>` | voting, procedures, link graph |
| `memory embed-build` | rebuild ngram embedding cache for all notes |
| `memory export-vectors [--path F]` | export vector index (id/content/kind/tags/embedding) to JSON |
| `memory list` / `memory lessons` | show memory-index / lessons+procedures |
| `memory export --vault <path>` | Obsidian export (notes/lessons/procedures + wikilinks) |
| `memory import --vault <path>` / `memory sync --vault <path> [--mode import\|export\|both]` | Obsidian round-trip / auto-sync |
| `skill list / search <q> / install <name\|owner/repo>` | skills management |
| `skill push --remote <url> [--skill all\|name] [--token]` | publish skills to a hub (auth via `ARGUS_HUB_TOKEN`) |
| `skill tap add/remove/list` | manage GitHub taps |
| `mcp add/remove/tools/call` / `serve` | MCP client (JSON-RPC stdio); hub + scheduler |
| `bench --model M` | smoke benchmark (100% acc) |
| `eval --evals <file|dir|list>` | GAIA-lite / GAIA-L1 subset, multi-file + per-file aggregate |
| `fusion "task" --workers N` | planner + worker pool |
| `run "…" --session <id>` | continue a saved session (seed = previous transcript) |
| `session` | list saved sessions |
| `session show/tail/search/rm/dedup/tui` | session browser (+ dedup by goal+transcript, drop empty) |
| `plugin add --event E --cmd C [--interval N]` / list / remove | hooks: before_step\|after_step\|on_done\|on_error\|timer (env ARGUS_*) |
| `task add/list/run/tui` | durable tasks — `task run` runs due tasks in parallel (multi-session) |
| `serve --tick S` | daemon: skill hub + auto-runs due tasks |

## Modes & safety

- `--mode plan` — read-only; every write tool refused.
- `--mode auto` — file writes inside the workspace don't ask.
- `--mode bypass` — nothing asks (session-only, never persisted).
- `--yes` — approve dangerous calls (`file.write`, `shell`, `skill.run`).
- Modes are session state: a bypass never survives a restart.
- `http.get`, `browser.navigate`, `browser.get` are SSRF-guarded (private/loopback blocked).

## Memory model

Plain JSON in `<stateDir>/memory/`:
- `profile.json` — keyword-gated facts (`pinned=true` always shown).
- `notes.json` — typed notes (event/behavior/knowledge/skill).
- `lessons.json` + `procedures.json` — distilled by consolidation (a tag seen
  ≥3 times produces a lesson + an advisory procedure).
- Prompt carries pointers (`### profile / lessons / procedures / memory-index`);
  full bodies are fetched via `memory.recall { id }` only when needed.
- Reflection (every 3 turns + final flush) extracts SET/NOTE lines automatically.

## Skills

SKILL.md playbooks (name/description/version/requires_tools/requires_scripts/
dangerous). Body loads on `skill.view` (KV-cache friendly); scripts run only
from `requires_scripts` and with approval. Sources: built-in registry,
GitHub taps (`owner/repo[/path]`), or a skill hub (`serve` + `browse --remote` /
`push --remote`). Browser recipes (web-research, form-fill, login-flow, …) install
with a ready `browser.flow` template.

## Browser (CDP)

`browser.navigate/click/type/snapshot/eval/flow` drive a real headless Chrome
via DevTools Protocol (WebSocket). `browser.flow` runs a multi-step scenario in
one call:
```json
{"steps":[{"op":"navigate","url":"https://…"},{"op":"type","selector":"#q","text":"x"},
          {"op":"click","selector":"button"},{"op":"snapshot"}]}
```

## Eval

`evals/gaia_lite.md` (5 tasks) and `evals/gaia_l1_subset.md` (5 multi-step) —
reproducible with `argus-agent eval`. Results on qwen2.5:7b: smoke 100%,
GAIA-Lite 60%, GAIA-L1 subset 60% (see `benchmarks/`).

## Fusion

`fusion "task" --workers N`: a planner LLM splits the goal into JSON subtasks; a
pool of threads runs each worker with its own memory directory; results merge.

## State directory

`~/.argus-agent/` (override `ARGUS_STATE_DIR`): config.json, memory/, skills/,
taps.json, sessions/tasks (future). Everything is plain files — inspect or wipe
freely.
