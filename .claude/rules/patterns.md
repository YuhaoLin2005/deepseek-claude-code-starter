# Common Patterns

## Skeleton Projects

When implementing new functionality:
1. Search for battle-tested skeleton projects
2. Evaluate options via parallel agents (security, extensibility, relevance)
3. Clone best match as foundation, iterate within proven structure

## Repository Pattern

Encapsulate data access behind a consistent interface: `findAll`, `findById`, `create`, `update`, `delete`. Business logic depends on abstract interface, not storage mechanism. Enables easy data source swapping and simpler testing.

## API Response Format

Use a consistent envelope:
- `success` (boolean), `data` (nullable on error)
- `error` (nullable on success), `metadata` for pagination (`total`, `page`, `limit`)
