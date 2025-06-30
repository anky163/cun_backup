# gui/tabs/tab_planbreak.py

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
from plan_core import format_tasks

def create_tab_planbreak(notebook):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text='Chia Task')

    input_text = scrolledtext.ScrolledText(frame, height=10)
    input_text.pack(fill='x')

    output_text = scrolledtext.ScrolledText(frame, height=15)
    output_text.pack(fill='both', expand=True)

    def load_file():
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filepath:
            with open(filepath, encoding="utf-8") as f:
                input_text.delete('1.0', tk.END)
                input_text.insert(tk.END, f.read())

    def split_tasks():
        raw = input_text.get("1.0", tk.END).strip()
        tasks = [line.strip() for line in raw.splitlines() if line.strip()]
        output = format_tasks(tasks)
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, output)

    ttk.Button(frame, text="Tải từ file", command=load_file).pack()
    ttk.Button(frame, text="Chia Task", command=split_tasks).pack(pady=5)

    return frame
