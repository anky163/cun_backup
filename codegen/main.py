import sys
from code_core import gen_shell_cmd, gen_python_code

def usage():
    print("Usage:")
    print("  python3 main.py shell \"mô tả lệnh\"")
    print("  python3 main.py py \"mô tả lệnh\"")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    lang = sys.argv[1]
    desc = " ".join(sys.argv[2:])

    if lang == "shell":
        print(gen_shell_cmd(desc))
    elif lang == "py":
        print(gen_python_code(desc))
    else:
        usage()
