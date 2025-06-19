# respgen.py - phản hồi rule-based từ file ruleset

"""
Dưới đây là hướng dẫn test respgen.py (bản mới – dùng ruleset ngoài):

✅ 1. Tạo file rule resp_rules.txt
bash:
    nano resp_rules.txt

    Nội dung:
    hello → Chào mày. Cún đây.
    mày là ai → Tao là Cún, clone phản xạ offline.
    gâu → Gâu gâu con mẹ mày!
    bye → Tạm biệt. Cún ngồi im.
Lưu bằng Ctrl+O, Enter → thoát Ctrl+X.

✅ 2. Chạy respgen.py với input trực tiếp
bash:
    python3 respgen.py "hello"
→ Kết quả:
    Chào mày. Cún đây.

✅ 3. Test bằng nhập stdin
bash:
    python3 respgen.py
Nhập:
    mày là ai
→ Ctrl+D để kết thúc nhập
Kết quả:
    Tao là Cún, clone phản xạ offline.

✅ 4. Test fallback (không khớp)
bash:
    python3 respgen.py "sủa đi"
→
    Tao không hiểu mày nói gì.

✅ 5. Test case-insensitive
bash:
    python3 respgen.py "GÂU"
→
    Gâu gâu con mẹ mày!
"""


import sys
import os

RULEFILE = os.environ.get("RESP_RULES", "resp_rules.txt")


def load_rules(file_path):
    rules = []
    if not os.path.exists(file_path):
        print(f"Không tìm thấy file rule: {file_path}")
        return rules
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "→" in line:
                trig, resp = line.strip().split("→", 1)
                rules.append((trig.strip().lower(), resp.strip()))
    return rules

def respond(text, rules):
    text = text.lower()
    for trig, resp in rules:
        if trig in text:
            return resp
    return "Tao không hiểu mày nói gì."

def usage():
    print("Usage:")
    print("  python3 respgen.py \"câu hỏi\"")
    print("  hoặc không truyền gì để nhập bằng stdin (Ctrl+D kết thúc)")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        user_input = " ".join(sys.argv[1:])
    else:
        print("Nhập câu hỏi:")
        user_input = sys.stdin.read()
    rules = load_rules(RULEFILE)
    print(respond(user_input.strip(), rules))
