import sys
from log_core import add_log, grep_log, cat_log

def usage():
    print("Usage:")
    print("  python3 main.py add \"nội dung log\"")
    print("  python3 main.py grep \"term\"")
    print("  python3 main.py cat")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "add" and len(sys.argv) >= 3:
        content = " ".join(sys.argv[2:])
        ts = add_log(content)
        print(f"✅ Ghi log tại {ts}")
    elif cmd == "grep" and len(sys.argv) >= 3:
        term = " ".join(sys.argv[2:])
        results = grep_log(term)
        if results:
            for line in results:
                print(line)
        else:
            print("❌ Không có kết quả.")
    elif cmd == "cat":
        content = cat_log()
        if content:
            print(content)
        else:
            print("📭 Log trống.")
    else:
        usage()
