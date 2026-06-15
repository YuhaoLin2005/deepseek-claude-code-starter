# Claude Code Starter: DeepSeek + Windows (Batteries Included)

> A battle-tested Claude Code configuration for DeepSeek API on Windows. 8 MCP services, 9 custom agents, 3-layer auto-backup, local OCR, and RTK token optimization — everything you need to go from zero to productive in 15 minutes.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)](#)
[![Model: DeepSeek](https://img.shields.io/badge/Model-DeepSeek_v4_Pro-green.svg)](#)
[![RTK: 55% Savings](https://img.shields.io/badge/RTK-55%25_Token_Savings-purple.svg)](#)

[中文 README](README.md) | [Setup Guide](SETUP.md)

---

## Screenshots

| RTK Token Savings (55%) | Custom Agents (9) |
|:---:|:---:|
| ![RTK Gain](screenshots/02-rtk-gain.png) | ![Agents](screenshots/03-agents.png) |

---

## Why This Exists

Claude Code is powerful, but the gap between `npm install` and actually productive is filled with friction: finding the right MCP packages, permission popups everywhere, sub-agents using weak models, commands eating up tokens...

This repo is everything I figured out through trial and error — polished and ready to clone. **Not chasing perfection, just aiming for "it works comfortably."**

### Real Numbers

```bash
$ rtk gain --history

RTK Token Savings (Global Scope)
════════════════════════════════════════════════════════════
Total commands:    177
Input tokens:      39.1K
Output tokens:     17.9K
Tokens saved:      21.3K (54.4%)
Efficiency meter:  █████████████░░░░░░░░░░░ 54.4%
```

---

## What's Inside

| Category | Count | Details |
|----------|:-----:|---------|
| 🧩 **MCP Services** | 8 | Filesystem · Playwright · GitHub · PostgreSQL · Context7 (docs) · DuckDuckGo (search) · Parallel Search (multi-engine) · Squish (persistent memory) |
| 🤖 **Custom Agents** | 9 | Code Review · Security Audit · TDD Guide · Architecture · Build Debugger · Code Simplifier · Docs Updater · Rust Reviewer · Senior Dev |
| 📋 **Rule Files** | 6 | Code Quality · Security · Testing · Workflow · Performance · Design Patterns |
| 🛡️ **Auto-Backup** | 3 layers | Hook-level file backup (pre-edit snapshots) · SessionStart git commit · Manual git fallback |
| ⚡ **RTK Integration** | — | Shell command optimization, measured 55% token savings |
| 🚀 **Parallel Execution** | — | Sub-agent pool + multi-engine parallel search — independent tasks run simultaneously |
| 🔍 **Local OCR** | — | EasyOCR offline screenshot text extraction, no API key, 85%+ Chinese accuracy |
| 🧠 **Smart Prompts** | — | Context-aware suggestions in Chinese for available skills |
| 🪟 **Windows Friendly** | — | MCP paths, RTK hooks, Python environment — all the Windows-specific gotchas solved |

---

## Quick Start

```bash
# 1. Get DeepSeek API Key → https://platform.deepseek.com
# 2. Clone this repo
git clone https://github.com/YuhaoLin2005/claude-code-starter.git
cd claude-code-starter

# 3. Copy config files
cp -r .claude/rules/ ~/.claude/rules/
cp -r .claude/agents/ ~/.claude/agents/
cp -r .claude/commands/ ~/.claude/commands/
cp .claude/CLAUDE.md ~/.claude/
cp .claude/RTK.md ~/.claude/

# 4. Configure MCP servers
cp templates/mcp.json.example ~/.mcp.json
# Edit ~/.mcp.json — update filesystem paths to your own

# 5. Set environment variables
#    Windows: setx ANTHROPIC_API_KEY "sk-your-deepseek-key"
#    Mac/Linux: export ANTHROPIC_API_KEY="sk-your-deepseek-key"

# 6. Restart Claude Code
```

📖 **[Detailed Setup Guide (Chinese)](SETUP.md)** · ❓ [Report Issue](https://github.com/YuhaoLin2005/claude-code-starter/issues)

---

## Lessons Learned

Things that cost me hours. May save you some:

- **Sub-agent quality** — Default uses flash model for sub-tasks. Set `CLAUDE_CODE_SUBAGENT_MODEL=deepseek-v4-pro` to force the main model.
- **Cache hit rate (the WHY)** — Claude Code injects an `ATTRIBUTION_HEADER` (session ID, timestamp) into every request. DeepSeek's prompt cache sees these as different requests → ~50% hit rate. Set `CLAUDE_CODE_ATTRIBUTION_HEADER="0"` → jumps to 90%+. That's half the tokens saved per request.
- **Long context utilization** — DeepSeek V4 Pro has 1M context but conservative defaults. Use `autoCompactWindow=600K` + `CLAUDE_CODE_MAX_OUTPUT_TOKENS=32000` + `alwaysThinkingEnabled=true` for large refactors without context loss.
- **Parallel execution** — Independent tasks (multi-agent review, multi-engine search) run simultaneously via `parallel-search` MCP + sub-agent pooling. No more waiting in line.
- **Windows MCP paths** — Use double backslashes: `C:\\Users\\...`
- **RTK name collision** — crates.io has a same-name package `reachingforthejack/rtk` (Rust Type Kit). Don't install the wrong one.
- **Screenshot OCR** — DeepSeek can't handle images. mcp-vision (DashScope API) proved unstable. Switched to **EasyOCR** (`pip install easyocr`) — runs offline, no API key required. Script: `.claude/scripts/ocr.py`
- **PyTorch GPU** — QGIS's bundled Python has DLL conflicts (c10.dll 1114). Use a standalone Python install.

---

## About the Author

A junior-year university student studying Product Management, exploring AI-automated web novel writing. Most interested in the intersection of code and AI — not pure coding, not pure prompting, but understanding "how to use AI to write the right code."

This repo is a byproduct of personal tinkering. Shared in case it helps someone else skip the same headaches.

---

## Who This Is For

- **Beginners** — Skip the zero-to-one grind. Get a complete working environment immediately.
- **Experienced users** — Some config choices here (MCP combo, RTK integration, hook patterns, auto-backup) might offer a useful reference angle.
- This isn't the "best" setup. It's just the one that works well for me.

PRs and issues welcome — let's make this better together.

---

## Acknowledgments

Standing on the shoulders of many open-source projects and community contributors. Full list in [ATTRIBUTIONS.md](ATTRIBUTIONS.md). Thank you to every author.

## License

MIT
