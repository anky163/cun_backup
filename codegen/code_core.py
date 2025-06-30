def gen_shell_cmd(desc):
    desc = desc.lower()
    if "list file" in desc:
        return "ls -la"
    if "remove file" in desc:
        return "rm filename"
    if "print hello" in desc:
        return "echo 'Hello world'"
    return f"# TODO: convert '{desc}' to shell command\n"

def gen_python_code(desc):
    desc = desc.lower()
    if "print hello" in desc:
        return "print('Hello world')"
    if "read file" in desc:
        return (
            "with open('filename', 'r') as f:\n"
            "    data = f.read()\n"
            "    print(data)"
        )
    if "list file" in desc:
        return (
            "import os\n"
            "print(os.listdir('.'))"
        )
    return f"# TODO: convert '{desc}' to python code\n"
