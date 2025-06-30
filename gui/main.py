# gui_cun.py
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import subprocess
import os
import sys


# Thêm toàn bộ modules con để import được mọi thứ
MODULE_DIRS = ["planbreak", "memcore", "promptgen", "codegen", "logs", "respgen"]

for module in MODULE_DIRS:
    abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", module))
    if abs_path not in sys.path:
        sys.path.append(abs_path)

# ==========================
# Giao diện chính
# ==========================
root = tk.Tk()
root.title("Hệ Cún - Offline Assistant GUI")
root.geometry("800x650")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Import từng tab từ thư mục gui/tabs
from tabs import tab_respgen, tab_planbreak, tab_help

# Thêm từng tab vào giao diện chính
notebook.add(tab_respgen.build_tab(root), text='Cún trả lời')
notebook.add(tab_planbreak.create_tab_planbreak(notebook), text='Planbreak')
notebook.add(tab_help.build_tab(), text='Hướng dẫn')

root.mainloop()
