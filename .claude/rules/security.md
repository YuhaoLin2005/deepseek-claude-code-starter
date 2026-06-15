# Security

## Mandatory Checks (Before ANY Commit)

- [ ] No hardcoded secrets (API keys, passwords, tokens)
- [ ] All user inputs validated
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (sanitized HTML)
- [ ] CSRF protection enabled
- [ ] Auth verified, rate limiting on endpoints
- [ ] Error messages don't leak sensitive data

## Secret Management

- NEVER hardcode secrets in source code
- ALWAYS use environment variables or a secret manager
- Validate required secrets at startup
- Rotate any secrets that may have been exposed

## Security Review Triggers

STOP and use security-reviewer agent when modifying:
- Authentication / authorization code
- User input handling / database queries
- File system operations / external API calls
- Cryptographic operations / payment code

## Response Protocol

If security issue found:
1. STOP immediately
2. Use **security-reviewer** agent
3. Fix CRITICAL issues before continuing
4. Rotate any exposed secrets
5. Review entire codebase for similar issues

## Common Vulnerabilities to Catch

- Hardcoded credentials, SQL injection, XSS
- Path traversal, CSRF, authentication bypasses
- N+1 queries, missing pagination, unbounded queries
