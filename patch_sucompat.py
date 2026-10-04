#!/usr/bin/env python3
"""为 ReSukiSU 的 SUSFS 版 ksu_handle_faccessat 补回 uid 校验。

背景
----
CONFIG_KSU_SUSFS 模式下（本仓库实际生效的 hook 方式），sucompat 的
ksu_handle_faccessat() 缺少 ksu_is_allow_uid_for_current() 判断，会把
**任何进程**对 /system/bin/su 的 access()/faccessat() 改写成对
/system/bin/sh 的检查，于是“文件不存在但 access 报告存在”，检测软件
据此误报找到 su。

同一文件的另外两处（非 SUSFS 版 ksu_handle_faccessat、SUSFS 版
ksu_handle_stat）都保留了该判断，这里补回以保持一致：未授权进程得到
ENOENT（su 被隐藏），已授权 app / shell / su 域进程行为不变。

行为
----
- 幂等：已打补丁（含 MARKER）则直接返回 0；
- 锚点失配（上游代码结构变化）则返回 1 并报错，绝不静默跳过。
"""

import sys
from pathlib import Path

MARKER = "KSU_FACCESSAT_UID_CHECK"

# 只有 SUSFS 版签名带 struct filename **，非 SUSFS 版是 const char __user **，因此唯一
SIGNATURE = (
    "int ksu_handle_faccessat(int *dfd, struct filename **filename, "
    "int *mode, int *__unused_flags)"
)

# 函数体内紧随其后的开关判断，作为插入锚点
ANCHOR = """    if (!static_branch_unlikely(&ksu_su_compat_enabled)) {
        return 0;
    }
"""

INSERT = """
    /* KSU_FACCESSAT_UID_CHECK: 未授权进程必须看不到 /system/bin/su。
     * 否则 access()/faccessat() 会把 su 改写成 sh，检测软件据此误报 su 存在。
     * 与非 SUSFS 分支、以及本文件 SUSFS 版 stat 分支的判断保持一致。 */
    if (!ksu_is_allow_uid_for_current(ksu_get_uid_t(current_uid())))
        return 0;
"""


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: patch_sucompat.py <path/to/sucompat.c>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"[patch_sucompat] ERROR: 文件不存在: {path}", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8")

    if MARKER in text:
        print(f"[patch_sucompat] 已打过补丁，跳过: {path}")
        return 0

    sig_at = text.find(SIGNATURE)
    if sig_at < 0:
        print(
            "[patch_sucompat] ERROR: 未找到 SUSFS 版 ksu_handle_faccessat 签名，"
            "上游代码结构可能已变化，请人工核对后再更新本脚本。",
            file=sys.stderr,
        )
        return 1

    anchor_at = text.find(ANCHOR, sig_at)
    if anchor_at < 0:
        print(
            "[patch_sucompat] ERROR: 在目标函数体内未找到 static_branch 锚点，"
            "拒绝静默跳过。",
            file=sys.stderr,
        )
        return 1

    insert_at = anchor_at + len(ANCHOR)
    path.write_text(text[:insert_at] + INSERT + text[insert_at:], encoding="utf-8")
    print(f"[patch_sucompat] 补丁已应用: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
