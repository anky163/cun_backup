# planbreak/planbreak.py
import sys
import os
from plan_core import load_tasks_from_file, format_tasks

def resolve_input_file(arg):
    if os.path.exists(arg):
        return arg
    alt = os.path.join(os.path.dirname(__file__), arg)
    if os.path.exists(alt):
        return alt
    print(f"[✖] Không tìm thấy file: {arg} (đã thử cả {alt})")
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("❗ Usage: planbreak.py <task_file>")
        sys.exit(1)

    path = resolve_input_file(sys.argv[1])
    tasks = load_tasks_from_file(path)
    print("🧠 Task breakdown:")
    print(format_tasks(tasks))

if __name__ == "__main__":
    main()
