# Development Workflow

## Feature Implementation Pipeline

**0. Research & Reuse** (mandatory before new implementation)
- Search GitHub (`gh search code/repos`), npm/PyPI/crates.io for existing solutions
- Check library docs via Context7 or vendor docs
- Prefer battle-tested libraries and adaptable open-source implementations
- Port/wrap proven approaches over writing net-new code when it meets requirements

**1. Plan First** — Use **planner** agent; identify dependencies, risks, break into phases

**2. TDD** — Use **tdd-guide** agent; write tests first, implement to pass, verify 80%+

**3. Code Review** — Use **code-reviewer** agent immediately after writing code; address CRITICAL/HIGH issues

**3.5. Self-Check** — Complex logic first via **senior-dev** agent (self-reviews before output); then **code-reviewer** validates. Don't wait until the feature is complete — review incrementally per file/module.

**4. Commit & Push** — Detailed messages, conventional commits format

**5. Pre-Review Checks** — CI/CD passing, merge conflicts resolved, branch up to date

## Agent Usage

Available agents in `~/.claude/agents/`: **senior-dev**, **planner**, **architect**, **tdd-guide**, **code-reviewer**, **security-reviewer**, **build-error-resolver**, **doc-updater**, **rust-reviewer**

No user prompt needed:
- Complex implementation → **senior-dev** | Complex features → **planner**
- Architectural decisions → **architect** | Code just written → **code-reviewer**
- Bug fix / new feature → **tdd-guide**
- Security-sensitive code → **security-reviewer** | Build fails → **build-error-resolver**

ALWAYS use parallel execution for independent tasks. For complex problems, use split-role sub-agents (senior engineer, security expert, consistency reviewer).

## Proactive Skill Triggers (CRITICAL)

User won't remember to invoke skills manually. You MUST proactively suggest the right skill when you detect these situations. Don't silently skip — ask with a one-liner suggestion.

| Situation | Skill to suggest | Prompt |
|-----------|-----------------|--------|
| User describes a new feature or domain concept | `/grill-with-docs` | "要不要先用 grill-with-docs 把领域知识记录下来？" |
| User reports a bug or problem | `/triage` | "先用 triage 分类一下这个问题？" |
| About to start coding a feature | `/tdd` | "用 TDD 流程来做？先写测试再实现。" |
| Large PRD or spec needs breakdown | `/to-issues` | "这个 PRD 挺大的，拆成 issues 再逐个实现？" |
| Problem is vague, need to clarify | `/diagnose` | "问题还不明确，用 diagnose 深入分析一下？" |
| Multi-system or architectural change | `/zoom-out` | "涉及多个系统，先 zoom-out 看看整体架构？" |
| Need a quick proof-of-concept | `/prototype` | "先 prototype 快速验证可行性？" |
| Project missing domain context | Suggest creating `CONTEXT.md` | "这个项目还没有 CONTEXT.md，建一个方便后续？" |
| Feature has implementation conflicts with existing ADRs | Flag ADR conflict explicitly | 按 domain.md 规则标注冲突 |

## Agent Skills — Domain Docs

Before exploring unfamiliar projects:
1. Check for `CONTEXT.md` at repo root — read it first
2. Check `docs/adr/` for relevant architectural decisions
3. If both missing and project is complex, suggest `/grill-with-docs`
4. When naming concepts, use the glossary from CONTEXT.md — don't invent synonyms

## Git

**Commit format:** `<type>: <description>` — types: feat, fix, refactor, docs, test, chore, perf, ci

**PR workflow:** Analyze full commit history → `git diff base...HEAD` → draft PR summary with test plan → push with `-u` if new branch
