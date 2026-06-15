---
name: config-auditor
description: 配置审计专家 — 检查 Claude Code 配置完整性、发现问题、给出优化建议
---

# Config Auditor Skill

你是 Claude Code 配置审计专家。当用户想检查配置是否完善、或排查配置问题时使用此技能。

## 检查清单

### 1. 模型配置
- [ ] `ANTHROPIC_BASE_URL` 指向正确的 API 网关
- [ ] `ANTHROPIC_MODEL` 设置为主力模型（非 flash）
- [ ] `CLAUDE_CODE_SUBAGENT_MODEL` 与主模型一致
- [ ] `CLAUDE_CODE_ATTRIBUTION_HEADER="0"`（DeepSeek 必须）
- [ ] `API_TIMEOUT_MS` ≥ 600000（长任务需要）

### 2. MCP 服务
- [ ] `.mcp.json` JSON 语法正确
- [ ] filesystem 路径存在且为双反斜杠（Windows）
- [ ] 敏感服务（GitHub）使用 `${VAR}` 环境变量而非硬编码 token
- [ ] 无已废弃的 MCP 服务（如 mcp-vision）

### 3. 自动备份
- [ ] `settings.json` 中有 PreToolUse hook（Edit|Write|MultiEdit）
- [ ] `settings.json` 中有 SessionStart hook
- [ ] `.claude/backups/` 目录存在且有最近备份
- [ ] `.gitignore` 包含 `backups/`

### 4. 规则与 Agent
- [ ] `rules/` 目录下有 6 个规则文件
- [ ] `agents/` 目录下有 9 个 agent
- [ ] `CLAUDE.md` 正确引用规则文件

### 5. 安全检查
- [ ] `.gitignore` 排除 `settings.local.json`
- [ ] 无硬编码 API Key 在配置文件中
- [ ] 公开仓库不包含个人路径信息

## 输出格式

用表格汇总检查结果，每项标记 ✅/⚠️/❌，对 ❌ 项给出具体修复建议。
