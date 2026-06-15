# Claude Code + DeepSeek: The Missing Config Layer

> **For developers using Claude Code CLI with DeepSeek API.** Not a fork, not a wrapper — a battle-tested configuration layer that bridges the gap between `npm install` and actually productive.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)](#)
[![Model: DeepSeek](https://img.shields.io/badge/Model-DeepSeek_v4_Pro-green.svg)](#)
[![RTK: 55% Savings](https://img.shields.io/badge/RTK-55%25_Token_Savings-purple.svg)](#)

[中文 README](README.md) · [Setup Guide (Chinese)](SETUP.md)

---

## Before You Star — Read This First

### What This Repo Is

**Between "Claude Code CLI" and "DeepSeek API" there's a missing layer of engineering glue** — MCP service configs, cache tuning, sub-agent model selection, backup strategies. This repo is that glue.

It is NOT a Claude Code fork. It is NOT a DeepSeek wrapper. It is a **configuration + toolchain layer** that sits on top of both.

### Three-Layer Architecture: Who Does What

```
┌──────────────────────────────────────────────────┐
│          This Repo (Config & Tooling)              │
│  MCP Services · Custom Agents · Rules · Hooks      │
│  RTK Token Savings · Auto-Backup · OCR             │
│  → Problems here? File an Issue                    │
├──────────────────────────────────────────────────┤
│         Claude Code CLI (Tool Layer)               │
│  Agent Loop · Tool Calling · Permissions · UI      │
│  → Maintained by Anthropic. Not our scope.         │
├──────────────────────────────────────────────────┤
│          DeepSeek API (Model Layer)                │
│  LLM Inference · Prompt Cache · Token Billing      │
│  → Provided by DeepSeek. We only adapt configs.    │
└──────────────────────────────────────────────────┘
```

**This layering matters — so you know where to go when something breaks:**

| Symptom | Which Layer | Where to Look |
|---------|------------|---------------|
| CLI hangs, tool call errors | Claude Code CLI | [anthropics/claude-code](https://github.com/anthropics/claude-code) |
| Poor model output, API 500s | DeepSeek API | [platform.deepseek.com](https://platform.deepseek.com) |
| MCP won't start, Agent broken | This repo's config | [File an Issue](https://github.com/YuhaoLin2005/claude-code-starter/issues) |

### Is This For You?

**✅ This repo is for you if:**

- You use **Claude Code CLI** — the `claude` command in a terminal. Not a VSCode extension. Not the web app. Not an API SDK.
- You use **DeepSeek API** as your LLM backend (cost-effectiveness, not desperation)
- You're on **Windows** (Mac/Linux works too, but you'll need to tweak paths)
- You want to skip the zero-to-one grind of MCP/Agent/Rules configuration
- You care about token costs and want 90%+ cache hit rates

**❌ This repo is NOT for you if:**

- You use **Cursor / Copilot / Windsurf / Trae** or any IDE plugin (those are entirely different tools)
- You use **Anthropic's official API** instead of DeepSeek (the cache fix and model configs won't apply)
- You expect **one-click, zero-config** setup (you'll need to edit 2 paths — this is CLI tooling, not SaaS)
- You want the "best" setup (this is the "battle-tested, definitely works" setup)
- You're on a **headless Linux server** (Playwright MCP needs a browser; headless isn't configured here)

---

## Four Problems This Solves

### ① DeepSeek Cache Hit Rate Stuck at ~50%

**Root cause**: Claude Code injects an `ATTRIBUTION_HEADER` containing a session ID and timestamp into every request. DeepSeek's prompt cache sees these as different requests → half your tokens are wasted.

**The fix**: Set `CLAUDE_CODE_ATTRIBUTION_HEADER="0"`. Cache hit rate jumps from **~50% → 90%+**. Every request costs half as much.

```bash
# Real numbers (RTK + cache hit rate combined)
$ rtk gain --history
Tokens saved: 21.3K (54.4%)
```

### ② Zero-to-Productive Takes Days, Not Minutes

Fresh `npm install -g @anthropic-ai/claude-code` gives you a bare CLI. No MCP services. No custom agents. No rules. Everyone reinvents the same wheel.

**What's here**: 8 MCP services, 9 custom agents, 6 rule files — all configured, tested, and compatible with each other. **Clone → Copy → Edit 2 paths → Work.**

### ③ No Undo When AI Messes Up

AI edits are probabilistic. Without backups, every change is a gamble.

**Three-layer automatic backup** — from per-edit snapshots to session-level git commits to manual rollback:

| Layer | Mechanism | When |
|-------|----------|------|
| File-level | PreToolUse Hook: auto-copy to `.claude/backups/` before every Edit/Write (keeps last 5) | Before every edit |
| Session-level | SessionStart Hook: auto `git commit` all uncommitted changes | Every session start |
| Manual | `git reset --hard HEAD~1` — instant rollback | Anytime |

### ④ Tokens Burned on Shell Output

`git status`, `npm install`, `ls -la` — the full output is piped to the model and billed as input tokens, even though most of it is noise to the AI.

**The fix**: RTK (Rust Token Killer) intelligently strips shell output to what the AI actually needs. **Measured: 55% token savings**.

---

## Vanilla Claude Code vs. This Config

| Dimension | Bare `npm install -g @anthropic-ai/claude-code` | With This Config |
|-----------|:--:|:--:|
| MCP Services | 0 (find, configure, debug yourself) | **8**, ready to go |
| Custom Agents | Built-in defaults | **9** specialized agents (review/security/TDD/architecture…) |
| Sub-agent Model | flash (weak on complex tasks) | **Forced pro model** |
| Cache Hit Rate | ~50% (ATTRIBUTION_HEADER interference) | **90%+** (fixed) |
| Auto-Backup | ❌ None | **3 layers** |
| Token Optimization | ❌ None | **RTK: 55% savings** |
| Windows Paths | ⚠️ DIY | **Pre-fixed** |
| Secret Scanning | ❌ None | **4-level desensitize scan** |
| Time to Productive | Days (trial and error) | **~15 minutes** |

---

## Quick Start

```bash
# 1. Get a DeepSeek API Key → https://platform.deepseek.com
# 2. Clone this repo
git clone https://github.com/YuhaoLin2005/claude-code-starter.git
cd claude-code-starter

# 3. Copy config files
cp -r .claude/* ~/.claude/
cp templates/mcp.json.example ~/.mcp.json

# 4. Edit ~/.mcp.json — update filesystem paths (the only manual step)
#    Find "C:\\Users\\xxx" → replace with your username

# 5. Set your API key
#    Windows: setx ANTHROPIC_API_KEY "sk-your-deepseek-key"
#    Mac/Linux: export ANTHROPIC_API_KEY="sk-your-deepseek-key"
#    Restart your terminal afterward

# 6. Launch
claude
```

> 📖 **Stuck?** The [detailed setup guide (Chinese)](SETUP.md) covers every step with screenshots.
>
> ⚠️ **RTK is optional** — everything works without it. It saves 55% on shell output tokens. Install: see [SETUP.md Step 5](SETUP.md#step-5安装-rtk可选推荐).

---

## What's Inside

| Category | Contents |
|----------|---------|
| 🧩 **MCP Services** (8) | Filesystem · Playwright Browser · GitHub API · PostgreSQL · Context7 Docs · DuckDuckGo Search · Parallel Multi-Engine Search · Squish Persistent Memory |
| 🤖 **Custom Agents** (9) | Code Review · Security Audit · TDD Guide · Architecture Design · Build Debugger · Code Simplifier · Docs Updater · Rust Reviewer · Senior Dev |
| 📋 **Rule Files** (6) | Code Quality · Security · Testing · Workflow · Performance · Design Patterns |
| 🛡️ **Auto-Backup** (3 layers) | PreToolUse file snapshots · SessionStart git commit · Manual git reset |
| ⚡ **Token Optimization** | RTK shell output stripping (measured 55%) · Cache hit rate fix (50%→90%+) · Sub-agent pro model |
| 🔍 **Local OCR** | EasyOCR offline screenshot recognition — DeepSeek can't handle images, this bridges the gap |
| 🔒 **Secret Scanning** | `/desensitize` command — scan for keys, paths, internal IPs before pushing (4 severity levels, allowlist support) |
| ⌨️ **Keybindings** | `Alt+T` toggle thinking mode · `Ctrl+O` view reasoning trace |

---

## 📸 Screenshots

| RTK Token Savings (55%) | Custom Agents (9) |
|:---:|:---:|
| ![RTK Gain](screenshots/02-rtk-gain.png) | ![Agents](screenshots/03-agents.png) |

---

## Design Decisions

Answers to questions you might have:

**Why not store API keys in `settings.local.json`?**
→ Environment variables have a single source of truth. `settings.local.json` in your home directory is one `git add -A` away from being committed.

**Why force the pro model for sub-agents?**
→ DeepSeek's flash model produces noticeably worse output on complex reasoning tasks (code review, security analysis). The tokens you save aren't worth the bugs you ship.

**Why hooks instead of cron for auto-backup?**
→ Hooks fire inside the Claude Code process, triggered by actual Edit/Write events. Cron is time-based — it won't save you if things break mid-session.

**Why EasyOCR over mcp-vision?**
→ mcp-vision depends on the DashScope API (unstable auth, requires internet). EasyOCR runs locally, no API key, 85%+ accuracy on Chinese text. Good enough.

**Why `~/.claude/` instead of per-project `.claude/`?**
→ Rules, agents, and habits are user-level concerns. Cloning configs into every project is wasteful and leads to version fragmentation.

---

## Lessons Learned

Things that cost me hours. May save you some:

- **Sub-agent quality** — Default flash model for sub-tasks. Set `CLAUDE_CODE_SUBAGENT_MODEL=deepseek-v4-pro`.
- **Cache hit rate (the WHY)** — `ATTRIBUTION_HEADER` carries session ID + timestamp. DeepSeek cache sees them as distinct requests. Set to `"0"` → 50%→90%+.
- **Long context** — `autoCompactWindow=600K` + `CLAUDE_CODE_MAX_OUTPUT_TOKENS=32000` + `alwaysThinkingEnabled=true`.
- **Windows MCP paths** — Double backslashes: `C:\\Users\\...`, or JSON parsing fails.
- **RTK name collision** — crates.io has `reachingforthejack/rtk` (Rust Type Kit). You want the `rtk` package.
- **Screenshot OCR** — DeepSeek can't do vision. EasyOCR runs offline, no API key. Script: `.claude/scripts/ocr.py`.
- **PyTorch GPU on Windows** — QGIS's bundled Python has DLL conflicts (`c10.dll 1114`). Use a standalone Python install.

---

## Acknowledgments

Standing on the shoulders of many open-source projects and community contributors. Full list in [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

## License

MIT
