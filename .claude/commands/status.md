---
description: 查看 Claude Code 配置状态总览
---

# /status — 配置状态总览

快速查看当前 Claude Code 所有配置的状态。

## 检查项

1. **模型配置** — 当前使用的模型、API endpoint
2. **MCP 服务** — 列出所有 MCP 服务及连接状态
3. **Agent 列表** — `ls ~/.claude/agents/` 统计数量和文件名
4. **规则文件** — `ls ~/.claude/rules/` 列出所有规则
5. **RTK 状态** — `rtk gain` 显示 token 节省统计
6. **Git 备份** — 检查 `~/.claude/backups/` 目录和最近备份文件
7. **环境变量** — 检查关键环境变量是否设置（不显示具体值）

## 输出格式

用表格汇总以上各项的检查结果，每项标记 ✅/⚠️/❌。
