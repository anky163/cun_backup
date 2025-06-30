# respgen.py - chạy qua terminal để hỏi & học phản xạ
from resp_core import get_response, learn_response

def main():
    try:
        while True:
            inp = input("⚡ Nhập trigger: ").strip()
            if not inp:
                continue
            reply = get_response(inp)
            if reply:
                print(f"🧠 Phản hồi: {reply}")
            else:
                print("🤖 Tao không hiểu, mày muốn tao trả lời thế nào?")
                new_resp = input("💬 Nhập phản hồi mong muốn: ").strip()
                if new_resp:
                    learn_response(inp, new_resp)
                    print("✅ Đã học phản xạ mới.")
    except KeyboardInterrupt:
        print("\n👋 Thoát.")

if __name__ == "__main__":
    main()
