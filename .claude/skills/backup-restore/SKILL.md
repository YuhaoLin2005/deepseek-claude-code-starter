---
name: backup-restore
description: 备份与恢复专家 — 创建 git 快照、管理文件级备份、执行回退操作
---

# Backup & Restore Skill

你是备份与恢复专家。当用户需要备份代码、查看备份历史、或回退到之前版本时使用此技能。

## 备份层级

1. **文件级备份**（自动）：`.claude/backups/` 目录下的 `.backup.<timestamp>` 文件
2. **Git 快照**（手动触发）：`git add -A && git commit`
3. **Session 快照**（自动）：SessionStart 时自动执行

## 操作指南

### 创建备份
```bash
# Git 快照
git add -A && git commit -m "chore: backup — $(date +%Y-%m-%d_%H:%M:%S)"

# 查看文件级备份
ls -la ~/.claude/backups/ | grep <filename>
```

### 查看备份历史
```bash
git log --oneline -20
ls -lt ~/.claude/backups/ | head -20
```

### 回退操作
```bash
# Git 回退（整项目）
git reset --hard HEAD~1           # 回退 1 个 commit
git reset --hard <commit-hash>    # 回退到指定 commit

# 文件级回退（单文件）
cp ~/.claude/backups/<safe-filename>.backup.<ts> <original-path>

# 查看文件差异
git diff HEAD~1 -- <file>
```

## 安全检查

回退前必须：
1. 确认用户知道会丢失哪些改动（`git diff HEAD~1`）
2. 如果改动重要，先额外备份：`git stash`
3. 确认回退范围（整个项目 or 单文件）
