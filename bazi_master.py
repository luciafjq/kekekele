#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""综合八字命理大师 —— 命令行入口

用法:
    python3 bazi_master.py <阳历年> <阳历月> <阳历日> <时辰(0-23)> [--female]

内部调用 engine/bazi.py（改造自开源项目 china-testing/bazi）完成实际排盘与
古籍评判计算，本文件只负责调用、清理 ANSI 颜色码并输出可读文本，供命理大师
智能体（见 SKILL.md）在此基础上做进一步的白话解读。
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent / "engine"
ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def run_engine(year: int, month: int, day: int, hour: int, female: bool) -> str:
    cmd = [sys.executable, "bazi.py", "-g", str(year), str(month), str(day), str(hour)]
    if female:
        cmd.append("-n")
    proc = subprocess.run(
        cmd, cwd=str(ENGINE_DIR), capture_output=True, text=True, check=True
    )
    return ANSI_RE.sub("", proc.stdout)


def main():
    parser = argparse.ArgumentParser(description="综合八字命理大师 - 排盘引擎")
    parser.add_argument("year", type=int, help="阳历出生年")
    parser.add_argument("month", type=int, help="阳历出生月")
    parser.add_argument("day", type=int, help="阳历出生日")
    parser.add_argument("hour", type=int, help="出生时辰（24小时制，0-23）")
    parser.add_argument("--female", action="store_true", help="女命（默认男命）")
    args = parser.parse_args()

    output = run_engine(args.year, args.month, args.day, args.hour, args.female)
    print(output)


if __name__ == "__main__":
    main()
