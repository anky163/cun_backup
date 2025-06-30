# gui/tabs/tab_help.py
import tkinter as tk
from tkinter import scrolledtext

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
- Nhập câu hỏi → nhận câu trả lời theo rule-based (và học thêm nếu chưa biết)

---
Hệ thống chạy thuần Python 3, không phụ thuộc AI. Tối ưu cho CLI nhưng hỗ trợ GUI để dễ thao tác.
"""

def build_tab():
    frame = tk.Frame()
    help_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD)
    help_text.pack(fill='both', expand=True)
    help_text.insert(tk.END, HELP_TEXT)
    help_text.configure(state='disabled')
    return frame
