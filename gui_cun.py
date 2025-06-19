# gui_cun.py
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import subprocess
import os

# ==========================
# Hằng số đường dẫn file
# ==========================
HELP_TEXT = """
# Hướng dẫn sử dụng hệ Cún

## 1. Chia Task (planbreak)
- Nhập mô tả mục tiêu → tự động phân nhỏ thành task

### Dùng:
- Nhập text → nhấn "Chia Task"
- Hoặc chọn file `.txt` rồi chạy

## 2. Quản lý Memory (memcore)
- Lưu thông tin dạng key-value (kiểu "tên" - "giá trị")

### Dùng:
- Nhập key + value → [Thêm]
- Nhập key → [Lấy]
- Nhập từ khoá → [Tìm]
- [Xuất toàn bộ] sẽ in toàn bộ log

## 3. Tạo Prompt (prompt_engine)
- Dùng khung sẵn, điền biến → tạo prompt chuẩn để hỏi LLM (nếu cần)

### Dùng:
- Lưu khung prompt: đặt tên template, nhập prompt có {placeholder}
- Tạo prompt: nhập biến theo dạng key=value, dùng template

## 4. Sinh Code (codegen)
- Nhập lệnh tự nhiên → ra shell hoặc python script

## 5. Ghi Log (mdlog)
- Ghi chú nhanh vào `logs.md` dạng markdown

## 6. Cún trả lời (respgen)
- Nhập câu hỏi → nhận câu trả lời theo rule-based

---
Hệ thống chạy thuần Python 3, không phụ thuộc AI. Tối ưu cho CLI nhưng hỗ trợ GUI để dễ thao tác.
"""

# ==========================
# Hàm tiện ích
# ==========================
def run_cmd(command):
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Lỗi: {e.output}"

# ==========================
# Giao diện chính
# ==========================
root = tk.Tk()
root.title("Hệ Cún - Offline Assistant GUI")
root.geometry("800x650")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# ===== TAB 1: planbreak =====
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text='Chia Task')

input_text = scrolledtext.ScrolledText(frame1, height=10)
input_text.pack(fill='x')

def load_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, encoding="utf-8") as f:
            input_text.delete('1.0', tk.END)
            input_text.insert(tk.END, f.read())

output_text = scrolledtext.ScrolledText(frame1, height=15)
output_text.pack(fill='both', expand=True)

ttk.Button(frame1, text="Tải từ file", command=load_file).pack()
ttk.Button(frame1, text="Chia Task", command=lambda: output_text.delete('1.0', tk.END) or output_text.insert(tk.END, run_cmd(f"echo \"{input_text.get('1.0', tk.END)}\" | python3 planbreak.py"))).pack(pady=5)

# ===== TAB 2: Memory =====
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text='Memory')

mem_key = tk.Entry(frame2)
mem_key.pack(fill='x')
mem_val = tk.Entry(frame2)
mem_val.pack(fill='x')

mem_output = scrolledtext.ScrolledText(frame2, height=15)
mem_output.pack(fill='both', expand=True)

ttk.Button(frame2, text="Thêm", command=lambda: mem_output.insert(tk.END, run_cmd(f"python3 memcore.py add \"{mem_key.get().strip()}\" \"{mem_val.get().strip()}\"\n"))).pack()
ttk.Button(frame2, text="Lấy", command=lambda: mem_output.insert(tk.END, run_cmd(f"python3 memcore.py get \"{mem_key.get().strip()}\"\n"))).pack()
ttk.Button(frame2, text="Tìm", command=lambda: mem_output.insert(tk.END, run_cmd(f"python3 memcore.py grep \"{mem_key.get().strip()}\"\n"))).pack()
ttk.Button(frame2, text="Xuất toàn bộ", command=lambda: mem_output.insert(tk.END, run_cmd("python3 memcore.py dump\n"))).pack()

# ===== TAB 3: Prompt =====
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text='Prompt')

template_name = tk.Entry(frame3)
template_name.insert(0, 'default')
template_name.pack(fill='x')

prompt_input = scrolledtext.ScrolledText(frame3, height=8)
prompt_input.pack(fill='x')

prompt_vars = tk.Entry(frame3)
prompt_vars.pack(fill='x')
prompt_output = scrolledtext.ScrolledText(frame3, height=10)
prompt_output.pack(fill='both', expand=True)

ttk.Button(frame3, text="Lưu Template", command=lambda: subprocess.run(f"echo \"{prompt_input.get('1.0', tk.END)}\" | python3 prompt_engine.py save {template_name.get().strip()}", shell=True)).pack()
ttk.Button(frame3, text="Tạo Prompt", command=lambda: prompt_output.insert(tk.END, run_cmd(f"python3 prompt_engine.py gen {template_name.get().strip()} {prompt_vars.get().strip()}\n"))).pack()

# ===== TAB 4: Codegen =====
frame4 = ttk.Frame(notebook)
notebook.add(frame4, text='Codegen')

lang_choice = tk.StringVar(value="shell")
ttk.Radiobutton(frame4, text="Shell", variable=lang_choice, value="shell").pack(anchor='w')
ttk.Radiobutton(frame4, text="Python", variable=lang_choice, value="py").pack(anchor='w')

code_input = tk.Entry(frame4)
code_input.pack(fill='x')

code_output = scrolledtext.ScrolledText(frame4, height=15)
code_output.pack(fill='both', expand=True)

ttk.Button(frame4, text="Sinh Code", command=lambda: code_output.insert(tk.END, run_cmd(f"python3 codegen.py {lang_choice.get()} \"{code_input.get()}\"\n"))).pack()

# ===== TAB 5: Ghi Log =====
frame5 = ttk.Frame(notebook)
notebook.add(frame5, text='Logs')

log_entry = tk.Entry(frame5)
log_entry.pack(fill='x')
log_output = scrolledtext.ScrolledText(frame5, height=15)
log_output.pack(fill='both', expand=True)

ttk.Button(frame5, text="Ghi log", command=lambda: log_output.insert(tk.END, run_cmd(f"python3 mdlog.py add \"{log_entry.get()}\"\n"))).pack()
ttk.Button(frame5, text="Xem toàn bộ", command=lambda: log_output.insert(tk.END, run_cmd("python3 mdlog.py cat\n"))).pack()

# ===== TAB 6: Cún trả lời =====
frame6 = ttk.Frame(notebook)
notebook.add(frame6, text='Cún trả lời')

resp_input = scrolledtext.ScrolledText(frame6, height=5)
resp_input.pack(fill='x')

resp_output = scrolledtext.ScrolledText(frame6, height=15)
resp_output.pack(fill='both', expand=True)

ttk.Button(frame6, text="Gâu!", command=lambda: resp_output.insert(tk.END, run_cmd(f"echo \"{resp_input.get('1.0', tk.END)}\" | python3 respgen.py\n"))).pack()

# ===== TAB 7: Hướng dẫn =====
frame7 = ttk.Frame(notebook)
notebook.add(frame7, text='Hướng dẫn')

help_text = scrolledtext.ScrolledText(frame7, wrap=tk.WORD)
help_text.pack(fill='both', expand=True)
help_text.insert(tk.END, HELP_TEXT)
help_text.configure(state='disabled')

root.mainloop()
