import sys
from mem_core import add_mem, get_mem, grep_mem, dump_mem

def usage():
    print("Usage:\n  python3 main.py add <key> <value>\n  get <key>\n  grep <term>\n  dump")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "add" and len(sys.argv) >= 4:
        key = sys.argv[2]
        value = " ".join(sys.argv[3:])
        add_mem(key, value)
        print(f"✅ Added/Updated key '{key}'")
    elif cmd == "get" and len(sys.argv) == 3:
        value = get_mem(sys.argv[2])
        print(value if value else f"Key '{sys.argv[2]}' not found.")
    elif cmd == "grep" and len(sys.argv) == 3:
        results = grep_mem(sys.argv[2])
        if results:
            for k, v in results.items():
                print(f"{k}:\n{v}\n{'-'*20}")
        else:
            print("❌ Không tìm thấy kết quả.")
    elif cmd == "dump":
        data = dump_mem()
        for k, v in data.items():
            print(f"## {k}\n{v}\n")
    else:
        usage()
