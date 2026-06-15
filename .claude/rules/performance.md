# Performance

## Model Selection (DeepSeek)

- **deepseek-v4-pro**: Main model + all subagents (via CLAUDE_CODE_SUBAGENT_MODEL)
- **deepseek-v4-flash**: Lightweight tasks only when explicitly configured per-agent

## Context Window Management

- 1M context available; auto-compact at 600K
- Keep large refactoring and multi-file features in the first 80% of context
- Single-file edits and simple fixes have lower context sensitivity

## Extended Thinking + Plan Mode

- Extended thinking enabled by default (up to 32K reasoning tokens)
- Toggle: Alt+T | Verbose view: Ctrl+O
- For complex tasks: enable Plan Mode, use multiple critique rounds, split-role sub-agents

## Build Troubleshooting

If build fails:
1. Use **build-error-resolver** agent
2. Analyze error messages
3. Fix incrementally, verify after each fix
