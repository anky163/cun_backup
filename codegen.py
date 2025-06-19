# codegen.py
"""
codegen.py - sinh script shell hoặc python từ lệnh dạng tự nhiên đơn giản
- input: câu mô tả ngắn
- output: script shell hoặc python
- mở rộng dễ dàng thêm rule hoặc template

Usage:
  python3 codegen.py shell "lệnh mô tả"
  python3 codegen.py py "lệnh mô tả"
"""

"""
Xài thử:
python3 codegen.py shell "print hello"
# ra:
echo 'Hello world'

python3 codegen.py py "read file"
# ra:
with open('filename', 'r') as f:
    data = f.read()
    print(data)

"""


import sys

def gen_shell_cmd(desc):
    # Rule đơn giản demo, map keyword -> shell cmd
    if "list file" in desc.lower():
        return "ls -la"
    if "remove file" in desc.lower():
        return "rm filename"
    if "print hello" in desc.lower():
        return "echo 'Hello world'"
    # default fallback
    return f"# TODO: convert '{desc}' to shell command\n"

def gen_python_code(desc):
    # Rule đơn giản demo, map keyword -> python snippet
    if "print hello" in desc.lower():
        return "print('Hello world')"
    if "read file" in desc.lower():
        return (
            "with open('filename', 'r') as f:\n"
            "    data = f.read()\n"
            "    print(data)"
        )
    if "list file" in desc.lower():
        return (
            "import os\n"
            "print(os.listdir('.'))"
        )
    # default fallback
    return f"# TODO: convert '{desc}' to python code\n"

def usage():
    print("Usage:")
    print("  python3 codegen.py shell \"mô tả lệnh\"")
    print("  python3 codegen.py py \"mô tả lệnh\"")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)
    lang = sys.argv[1]
    desc = sys.argv[2]
    if lang == "shell":
        print(gen_shell_cmd(desc))
    elif lang == "py":
        print(gen_python_code(desc))
    else:
        usage()


