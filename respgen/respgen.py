# respgen.py - phản xạ tự học bằng Trie + JSON ruleset
"""
Hướng dẫn sử dụng:

✅ 1. Chuẩn bị file rule dạng JSON:
    export RESP_RULES=resp_rules.json

✅ 2. Chạy trực tiếp:
    python3 respgen.py "hello"

✅ 3. Nhập stdin:
    python3 respgen.py
    > hello
    > Ctrl+D

✅ 4. Nếu chưa có prompt → sẽ hỏi lại và tự động cập nhật phản hồi cụ thể.
    📌 Lần đầu: trả lời fallback → gợi ý chỉnh sửa
    📌 Lần sau: sẽ nhớ phản hồi đã dạy

✅ 5. Cấu trúc JSON dạng Trie:
{
  "h": {"e": {"l": {"l": {"o": {"_": ["Chào mày", "Cún chào mày"]}}}}}
}

"""

import sys
import os
import json
import random
from trie import Trie

# ========= Cấu hình ========= #
RULEFILE = os.environ.get("RESP_RULES", "resp_rules.json")
FALLBACK_RESP = "Tao không hiểu mày nói gì."
PROMPT_PENDING_FILE = ".respgen_pending_prompt.txt"  # ghi tạm prompt cần phản hồi

# ========= Load Trie từ JSON ========= #
def load_trie(path):
    trie = Trie()
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                trie.from_dict(data)
            except json.JSONDecodeError:
                print("❌ File JSON lỗi. Dùng Trie rỗng.")
    return trie

# ========= Lưu Trie về JSON ========= #
def save_trie(trie, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(trie.to_dict(), f, ensure_ascii=False, indent=2)
    print(f"💾 Đã lưu phản hồi vào {path}")

# ========= Xử lý phản hồi ========= #
def respond(prompt, trie):
    prompt = prompt.lower().strip()

    # Check nếu đây là phản hồi cho một prompt trước đó
    if os.path.exists(PROMPT_PENDING_FILE):
        with open(PROMPT_PENDING_FILE, "r", encoding="utf-8") as f:
            pending_prompt = f.read().strip()
        os.remove(PROMPT_PENDING_FILE)

        if prompt:
            print(f"📌 Ghi nhận phản hồi mới cho: '{pending_prompt}' → '{prompt}'")
            trie.insert(pending_prompt, prompt)
            save_trie(trie, RULEFILE)
            return prompt
        else:
            return FALLBACK_RESP

    # Nếu là prompt bình thường → dò trie
    resp = trie.get(prompt)
    if resp:
        if isinstance(resp, list):
            return random.choice(resp)
        return resp

    # Fallback + gợi ý người dùng nhập lại prompt phản hồi
    print(FALLBACK_RESP)
    print(f"🔎 Không có rule rõ ràng cho: '{prompt}'")
    print("❓ Mày muốn tao phản hồi thế nào?")
    with open(PROMPT_PENDING_FILE, "w", encoding="utf-8") as f:
        f.write(prompt)
    return FALLBACK_RESP + "\n❓ Mày muốn tao phản hồi thế nào?"

# =====================================
# Xử lý nhập hàng loạt từ resp_bulk.json
# =====================================
def import_bulk_json(path, trie, save_path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            entries = json.load(f)
    except Exception as e:
        print(f"[❌] Lỗi đọc {path}: {e}")
        return

    added = 0
    for item in entries:
        # Nếu là output từ generate_variants.py (nested):
        if "original" in item and "variants" in item:
            all_items = [item["original"]] + item["variants"]
        else:
            all_items = [item]
        for pair in all_items:
            trig = pair.get("trigger", "").strip()
            resp = pair.get("response", "").strip()
            if trig and resp:
                trie.insert(trig, resp)
                added += 1

    save_trie(trie, save_path)
    print(f"[+] Đã import {added} cặp phản hồi từ {path}")
    return added

# ========= Main ========= #
def usage():
    print("Usage:")
    print("  python3 respgen.py 'câu hỏi'")
    print("  hoặc không truyền gì để nhập bằng stdin")


if __name__ == "__main__":
    if "--bulk" in sys.argv:
        bulk_path = sys.argv[sys.argv.index("--bulk") + 1]
        trie = load_trie(RULEFILE)
        import_bulk_json(bulk_path, trie, RULEFILE)
        sys.exit(0)
        
    if len(sys.argv) >= 2:
        user_input = " ".join(sys.argv[1:])
    else:
        user_input = sys.stdin.read()

    trie = load_trie(RULEFILE)
    print(respond(user_input.strip(), trie))
