#!/usr/bin/env python3
"""
Claude Code PreToolUse 安全阻断 hook。
检测敏感文件访问和危险命令，返回 exit code 2 时硬阻断操作。
"""

import json
import os
import sys

# ===== 敏感路径模式 =====
SENSITIVE_PATH_PATTERNS = [
    ".env",
    ".env.",
    "credentials",
    "secret",
    "token",
    "password",
    "~/.ssh/",
    ".ssh/",
    "~/.aws/",
    ".aws/credentials",
    "id_rsa",
    "private.key",
    ".pem",
]

# 精确排除：这些路径即使匹配也不是敏感的
ALLOWED_PATHS = [
    "settings.json",      # 我们的配置文件，允许修改
    ".mcp.json",          # MCP 配置
    ".claude/",           # 我们自己的配置目录
    "application.yml",    # SpringBoot 配置文件
    "pom.xml",           # Maven 配置
    "package.json",       # npm 配置
    ".env.example",       # 示例文件
    ".env.sample",
    "node_modules/",
    ".git/",
]

# ===== 危险命令模式 =====
DANGEROUS_COMMAND_PATTERNS = [
    ("rm -rf /", "递归删除根目录"),
    ("rm -rf ~", "递归删除家目录"),
    ("> /dev/sda", "覆盖磁盘设备"),
    ("mkfs.", "格式化文件系统"),
    ("git push --force origin main", "强制推送到 main"),
    ("git push --force origin master", "强制推送到 master"),
    ("git push -f origin main", "强制推送到 main（短参数）"),
    ("git push -f origin master", "强制推送到 master（短参数）"),
    ("chmod 777 /", "修改根目录权限"),
    ("chmod -R 777 /", "递归修改根目录权限"),
    ("curl", "网络下载管道执行"),
    ("wget", "网络下载"),
]


def is_path_allowed(file_path: str) -> bool:
    """检查路径是否在白名单中"""
    path_lower = file_path.lower()
    for allowed in ALLOWED_PATHS:
        if allowed.lower() in path_lower:
            return True
    return False


def check_sensitive_path(file_path: str) -> tuple:
    """检查文件路径是否敏感"""
    if is_path_allowed(file_path):
        return False, ""

    path_lower = file_path.lower()
    for pattern in SENSITIVE_PATH_PATTERNS:
        if pattern.lower() in path_lower:
            return True, f"SENSITIVE_PATH: {file_path} 匹配敏感模式 {pattern}"
    return False, ""


def check_dangerous_command(command: str) -> tuple:
    """检查命令是否危险"""
    # 管道执行检测（最危险模式）
    if "curl" in command and ("| bash" in command or "| sh" in command or "| sudo" in command):
        return True, f"DANGEROUS_PIPE: curl | bash/sudo 模式: {command[:80]}..."
    if "wget" in command and ("| bash" in command or "| sh" in command):
        return True, f"DANGEROUS_PIPE: wget | bash 模式: {command[:80]}..."

    for pattern, description in DANGEROUS_COMMAND_PATTERNS:
        if pattern in command:
            return True, f"DANGEROUS_CMD: {description}: {command[:80]}..."

    return False, ""


def main():
    tool_name = os.environ.get("CLAUDE_TOOL_NAME", "")
    tool_input_raw = os.environ.get("CLAUDE_TOOL_INPUT", "{}")

    try:
        tool_input = json.loads(tool_input_raw)
    except json.JSONDecodeError:
        tool_input = {}

    # === Read 工具：检查敏感文件路径 ===
    if tool_name in ("Read", "mcp__filesystem__read_file", "mcp__filesystem__read_text_file"):
        file_path = tool_input.get("file_path", "") or tool_input.get("path", "")
        if file_path:
            blocked, reason = check_sensitive_path(file_path)
            if blocked:
                print(f"[SECURITY-GUARD] BLOCKED: {reason}", file=sys.stderr)
                print("提示：如果确实需要访问此文件，请先确认它不包含密钥/密码。", file=sys.stderr)
                sys.exit(2)

    # === Bash 工具：检查危险命令 ===
    if tool_name == "Bash":
        command = tool_input.get("command", "")
        if command:
            blocked, reason = check_dangerous_command(command)
            if blocked:
                print(f"[SECURITY-GUARD] BLOCKED: {reason}", file=sys.stderr)
                print("提示：如果确实要执行此命令，请手动在终端中运行。", file=sys.stderr)
                sys.exit(2)

    # === Edit/Write 工具：检查目标路径 ===
    if tool_name in ("Edit", "Write", "mcp__filesystem__edit_file", "mcp__filesystem__write_file"):
        file_path = tool_input.get("file_path", "") or tool_input.get("path", "")
        if file_path:
            blocked, reason = check_sensitive_path(file_path)
            if blocked:
                print(f"[SECURITY-GUARD] BLOCKED: {reason}", file=sys.stderr)
                print("提示：如果确实需要修改此文件，请先确认它不包含密钥/密码。", file=sys.stderr)
                sys.exit(2)

    # 放行
    sys.exit(0)


if __name__ == "__main__":
    main()
