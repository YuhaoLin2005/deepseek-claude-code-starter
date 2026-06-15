---
description: 手动触发 git 备份快照
---

# /backup — 手动 Git 备份

对当前项目目录执行 `git add -A && git commit`，创建一个带时间戳的备份快照。

## 执行步骤

1. 执行 `git status` 检查当前状态
2. 如果有未提交变更，执行：
   ```bash
   git add -A && git commit -m "chore: manual backup — $(date +%Y-%m-%d_%H:%M:%S)"
   ```
3. 显示最近的 5 个 commit 记录
4. 如果 `~/.claude/backups/` 目录存在，也显示最新的 3 个文件级备份

## 输出

- 提交的 commit hash 和 message
- 最近 5 个 commit 摘要
- 文件级备份列表（如有）
