# Code Quality

## Immutability (CRITICAL)

ALWAYS create new objects, NEVER mutate existing ones. Immutable data prevents hidden side effects, makes debugging easier, and enables safe concurrency.

## Core Principles

- **KISS**: Simplest solution that works. Avoid premature optimization.
- **DRY**: Extract repeated logic into shared functions ONLY when repetition is real (≥3 occurrences), not speculative. See yagni.md ladder rung 1 before creating abstractions.
- **YAGNI**: Don't build features or abstractions before they're needed. Start simple, refactor when pressure is real.

## File & Function Organization

- Many small files > few large files. High cohesion, low coupling.
- Functions: <50 lines. Files: 200-400 typical, 800 max.
- Organize by feature/domain, not by type.
- Extract utilities from large modules.

## Error Handling & Validation

- Handle errors explicitly at every level. Never silently swallow.
- Validate all input at system boundaries. Fail fast with clear messages.
- Use schema-based validation where available. Never trust external data.

## Naming Conventions

- Variables/functions: `camelCase`. Booleans: `is/has/should/can` prefix.
- Interfaces/types/components: `PascalCase`. Constants: `UPPER_SNAKE_CASE`.

## Code Smells

- **Deep nesting**: Prefer early returns over nested conditionals (>4 levels).
- **Magic numbers**: Use named constants.
- **Long functions**: Split into focused pieces with clear responsibilities.

## Mandatory Self-Audit (Before Marking Complete)

After writing ANY function or module, you MUST perform this audit before considering the work done:

1. **Boundary scan**: List every input — what happens at null, empty string, zero, negative, max value, and concurrent access. Verify each case is either handled or explicitly rejected with a clear message.
2. **Null propagation trace**: Trace every variable from assignment to use — can it be null/undefined at any point? If yes, add a guard.
3. **Error path walk**: For every external call (API, DB, file I/O, network), trace what happens when it fails. No silent swallowing.
4. **SQL audit**: If you wrote a database query, confirm it uses parameterized queries — no string interpolation, no template literal injection.
5. **Security grep**: Scan your code for `password`, `token`, `key`, `secret`, `http://` — remove any hardcoded instances.

This is NOT optional. DeepSeek models have higher variance in instruction following — this self-audit compensates.

Before marking work complete:
- [ ] Code is readable and well-named
- [ ] Functions <50 lines, files <800 lines
- [ ] No deep nesting (>4 levels)
- [ ] Errors handled explicitly, no silent swallowing
- [ ] No hardcoded secrets, credentials, or debug statements
- [ ] Tests exist for new functionality (80%+ coverage)
- [ ] No mutation — immutable patterns used

## Review Severity

| Level | Meaning | Action |
|-------|---------|--------|
| CRITICAL | Security vulnerability or data loss | **BLOCK** merge |
| HIGH | Bug or significant quality issue | **WARN** before merge |
| MEDIUM | Maintainability concern | Consider fixing |
| LOW | Style/minor suggestion | Optional |

## Review Workflow

1. Run git diff to understand changes
2. Check security checklist first
3. Review code quality checklist
4. Run tests, verify coverage >= 80%
5. Use code-reviewer agent for detailed review
