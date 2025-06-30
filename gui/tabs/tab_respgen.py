import tkinter as tk
from tkinter import ttk, scrolledtext
from resp_core import get_response, learn_response

def build_tab(root):
    frame = ttk.Frame(root)

    resp_input = scrolledtext.ScrolledText(frame, height=5)
    resp_input.pack(fill='x')

    resp_output = scrolledtext.ScrolledText(frame, height=15)
    resp_output.pack(fill='both', expand=True)

    def handle_response():
        user_input = resp_input.get("1.0", tk.END).strip()
        print(f"prompt: @{user_input}@")
        if not user_input:
            return

        response = get_response(user_input)
        print(f"reply: @{response}@")
        if response:
            resp_output.insert(tk.END, f"🧠 {response}\n")
        else:
            resp_output.insert(tk.END, "🤖 Tao không hiểu, mày muốn tao trả lời thế nào?\n")
            def on_submit():
                new_resp = response_entry.get().strip()
                if new_resp:
                    learn_response(user_input, new_resp)
                    resp_output.insert(tk.END, "✅ Đã học phản xạ mới.\n")
                    popup.destroy()

            popup = tk.Toplevel(frame)
            popup.title("Nhập phản hồi mới")
            tk.Label(popup, text="💬 Phản hồi mong muốn:").pack()
            response_entry = tk.Entry(popup, width=60)
            response_entry.pack(padx=10, pady=5)
            ttk.Button(popup, text="Lưu", command=on_submit).pack(pady=5)

    ttk.Button(frame, text="Gâu!", command=handle_response).pack()
    return frame
