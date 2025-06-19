# prompt_engine.py
"""
prompt_engine.py - quản lý đa prompt template trong 1 file JSON
- save template: nhập prompt mẫu, đặt tên template
- gen prompt: chọn template, điền biến, xuất prompt hoàn chỉnh

Usage:
  python3 prompt_engine.py save [template_name]
  python3 prompt_engine.py gen [template_name] key=value ...

Nếu không có template_name thì dùng "default"
"""
"""
Cách dùng:

Lưu template mới:
    bash:
        python3 prompt_engine.py save task1
        Nhập prompt mẫu, Ctrl+D kết thúc.

Sinh prompt:
bash:
    python3 prompt_engine.py gen task1 key=value key2=value2
    Nếu không truyền tên template thì mặc định dùng "default"
"""

import sys
import json
import os

PROMPT_FILE = "prompt_template.json"

def load_data():
    if not os.path.exists(PROMPT_FILE):
        return {"templates": {}}
    try:
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # File rỗng hoặc lỗi đọc, khởi tạo mới
        return {"templates": {}}


def save_data(data):
    with open(PROMPT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_template(template_name):
    print(f"Nhập prompt template cho '{template_name}' (dùng {{key}} làm placeholder), Ctrl+D kết thúc:")
    content = sys.stdin.read()
    data = load_data()
    data["templates"][template_name] = content
    save_data(data)
    print(f"Đã lưu template '{template_name}' vào {PROMPT_FILE}")

def generate_prompt(template_name, vars_dict):
    data = load_data()
    templates = data.get("templates", {})
    template = templates.get(template_name)
    if not template:
        print(f"Template '{template_name}' không tồn tại. Có các template: {list(templates.keys())}")
        sys.exit(1)
    try:
        prompt = template.format(**vars_dict)
    except KeyError as e:
        print(f"Thiếu biến trong template: {e}")
        sys.exit(1)
    print(prompt)

def usage():
    print("Usage:")
    print("  python3 prompt_engine.py save [template_name]   # Nhập và lưu template")
    print("  python3 prompt_engine.py gen [template_name] key=value ...  # Generate prompt")
    print("Nếu không truyền template_name, dùng 'default'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "save":
        template_name = sys.argv[2] if len(sys.argv) > 2 else "default"
        save_template(template_name)
    elif cmd == "gen":
        if len(sys.argv) < 3:
            usage()
            sys.exit(1)
        template_name = sys.argv[2]
        vars_pairs = sys.argv[3:]
        vars_dict = {}
        for pair in vars_pairs:
            if '=' not in pair:
                print(f"Định dạng biến sai: {pair}")
                sys.exit(1)
            k,v = pair.split('=',1)
            vars_dict[k] = v
        generate_prompt(template_name, vars_dict)
    else:
        usage()

