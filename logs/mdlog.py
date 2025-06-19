# mdlog.py
"""
mdlog.py - ghi log markdown đơn giản, grep-friendly
- add: thêm entry mới (ghi timestamp tự động)
- grep: tìm từ khóa trong log
- cat: in toàn bộ logs.md

Usage:
  python3 mdlog.py add "nội dung"
  python3 mdlog.py grep "từ khóa"
  python3 mdlog.py cat
"""
"""
Ví dụ:

bash:
    python3 mdlog.py add "Test log đầu tiên: Cún viết xong markdown logger"

bash:
    python3 mdlog.py grep "Cún"
    
bash:
    python3 mdlog.py cat
"""


import sys
import time
import os

LOGFILE = os.environ.get("LOGFILE", "logs.md")

def add_entry(content):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    entry = f"## {timestamp}\n\n{content.strip()}\n\n---\n"
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"Đã ghi log tại {timestamp}")

def grep_entry(term):
    try:
        with open(LOGFILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            if term.lower() in line.lower():
                print(line.strip())
    except FileNotFoundError:
        print("Log chưa tồn tại.")

def cat_log():
    try:
        with open(LOGFILE, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Log trống.")

def usage():
    print("Usage:")
    print("  python3 mdlog.py add \"nội dung log\"")
    print("  python3 mdlog.py grep \"term\"")
    print("  python3 mdlog.py cat")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) >= 3:
        content = " ".join(sys.argv[2:])
        add_entry(content)
    elif cmd == "grep" and len(sys.argv) >= 3:
        grep_entry(" ".join(sys.argv[2:]))
    elif cmd == "cat":
        cat_log()
    else:
        usage()
