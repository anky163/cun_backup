import os

# === Gốc thư mục (cun_backup/) ===
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# === Đường dẫn tuyệt đối tới các file dữ liệu ===
MEMFILE = os.path.join(ROOT_DIR, "memcore", "mem.json")
LOGFILE = os.path.join(ROOT_DIR, "logs", "logs.md")
PROMPT_FILE = os.path.join(ROOT_DIR, "promptgen", "prompt_template.json")
RESP_RULES_FILE = os.path.join(ROOT_DIR, "respgen", "resp_rules.json")
TASK_DEFAULT_FILE = os.path.join(ROOT_DIR, "planbreak", "tasks.txt")

# === Tiện ích dùng chung ===
def resolve_path(*parts):
    return os.path.join(ROOT_DIR, *parts)
