# Claude Code Configuration

@RTK.md
@.claude/rules/code-quality.md
@.claude/rules/security.md
@.claude/rules/testing.md
@.claude/rules/workflow.md
@.claude/rules/performance.md
@.claude/rules/patterns.md

## Agent skills

### Issue tracker — PROACTIVE TRIGGERS
- User starts a new feature → create `.scratch/<feature-slug>/PRD.md`
- User reports a bug/problem → create `.scratch/<feature-slug>/issues/01-<slug>.md` with `Status: needs-triage`
- User asks "what's the status" → read and summarize issue files
- See `docs/agents/issue-tracker.md` for conventions

### Triage labels
Default vocabulary: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`.
- When creating an issue, ALWAYS add a `Status:` line
- When the user clarifies requirements, update the status accordingly
- See `docs/agents/triage-labels.md` for role mapping

### Domain docs
- Before working in a project, check for `CONTEXT.md` — read it if exists
- If project is complex and missing `CONTEXT.md`, suggest `/grill-with-docs`
- When you see unfamiliar terms, check `CONTEXT.md` glossary first
- See `docs/agents/domain.md` for conventions
