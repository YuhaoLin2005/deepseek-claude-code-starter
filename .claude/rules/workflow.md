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

## Git

**Commit format:** `<type>: <description>` — types: feat, fix, refactor, docs, test, chore, perf, ci

**PR workflow:** Analyze full commit history → `git diff base...HEAD` → draft PR summary with test plan → push with `-u` if new branch
