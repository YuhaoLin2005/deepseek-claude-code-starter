# Testing

## Minimum Coverage: 80%

Test types (ALL required):
1. **Unit Tests** — Individual functions, utilities, components
2. **Integration Tests** — API endpoints, database operations
3. **E2E Tests** — Critical user flows

## TDD Workflow (MANDATORY)

1. Write test first (RED) — it should FAIL
2. Write minimal implementation (GREEN) — it should PASS
3. Refactor (IMPROVE)
4. Verify coverage (80%+)

Use **tdd-guide** agent proactively for new features and bug fixes.

## Structure (AAA Pattern)

Arrange → Act → Assert:

```
test('descriptive name explaining behavior', () => {
  // Arrange
  const input = ...

  // Act
  const result = functionUnderTest(input)

  // Assert
  expect(result).toBe(expected)
})
```

Naming: describe the behavior — `test('returns empty array when no matches', () => {})`

## Troubleshooting

1. Use **tdd-guide** agent
2. Check test isolation
3. Verify mocks are correct
4. Fix implementation, not tests (unless tests are wrong)
