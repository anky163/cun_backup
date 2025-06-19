# memcore.py
# Hệ thống memory đơn giản dạng key-value store
# Chạy CLI Python 3, lưu data vào mem.json
# Dùng cho add/get/grep facts, dump toàn bộ
# Đơn giản, dễ grep, low RAM

import sys
import json
import os
import re

MEMFILE = os.environ.get("MEMFILE", "mem.json")

# Load data từ file JSON, trả về dict
def load_mem():
    if not os.path.exists(MEMFILE):
        return {}
    with open(MEMFILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return {}

# Lưu dict vào file JSON
def save_mem(data):
    with open(MEMFILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Thêm hoặc cập nhật key-value
def add_mem(key, value):
    data = load_mem()
    if key in data:
        # Nếu key đã tồn tại, nối thêm value cách nhau dấu newline
        data[key] += "\n" + value
    else:
        data[key] = value
    save_mem(data)
    print(f"Added/Updated key '{key}'")

# Lấy value theo key (exact match)
def get_mem(key):
    data = load_mem()
    if key in data:
        print(f"{key}:\n{data[key]}")
    else:
        print(f"Key '{key}' not found.")

# Tìm key hoặc value chứa từ khóa (case-insensitive)
def grep_mem(term):
    data = load_mem()
    term_lower = term.lower()
    found = False
    for k,v in data.items():
        if term_lower in k.lower() or term_lower in v.lower():
            print(f"{k}:\n{v}\n{'-'*20}")
            found = True
    if not found:
        print(f"No matches for '{term}' found.")

# Xuất toàn bộ dữ liệu dạng markdown để dễ đọc
def dump_mem():
    data = load_mem()
    print("# Memory Dump\n")
    for k,v in data.items():
        print(f"## {k}\n{v}\n")

# CLI interface
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:\n  memcore.py add <key> <value>\n  memcore.py get <key>\n  memcore.py grep <term>\n  memcore.py dump")
        sys.exit(1)

    cmd = sys.argv[1].lower()
    if cmd == "add" and len(sys.argv) >= 4:
        key = sys.argv[2]
        value = " ".join(sys.argv[3:])
        add_mem(key, value)
    elif cmd == "get" and len(sys.argv) == 3:
        get_mem(sys.argv[2])
    elif cmd == "grep" and len(sys.argv) == 3:
        grep_mem(sys.argv[2])
    elif cmd == "dump":
        dump_mem()
    else:
        print("Invalid command or arguments.")
        print("Usage:\n  memcore.py add <key> <value>\n  memcore.py get <key>\n  memcore.py grep <term>\n  memcore.py dump")

"""
Hướng dẫn sử dụng memcore.py:

Thêm nhớ:
python3 memcore.py add "bash cheat" "alias ll='ls -l'"

Lấy nhớ theo key:
python3 memcore.py get "bash cheat"

Tìm nhớ theo từ khóa:
python3 memcore.py grep "alias"

Xuất toàn bộ nhớ markdown:
python3 memcore.py dump
"""