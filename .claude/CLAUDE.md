# Claude Code Configuration

@RTK.md
@.claude/rules/code-quality.md
@.claude/rules/security.md
@.claude/rules/testing.md
@.claude/rules/workflow.md
@.claude/rules/performance.md
@.claude/rules/patterns.md

## Agent skills

### Issue tracker
Local markdown — issues and PRDs live as files under `.scratch/<feature-slug>/` in each project. See `docs/agents/issue-tracker.md`.

### Triage labels
Default label vocabulary — `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs
Single-context — one `CONTEXT.md` + `docs/adr/` per project root. See `docs/agents/domain.md`.
