# planbreak.py
# Mô-đun chia mục tiêu và ý đồ thành danh sách các task có thể thực hiện
# Phi-AI, chạy đơn thuần trên Python 3, RAM thấp. Dành cho hệ thống như của K.

import re
import sys

# ===== Danh sách từ khóa gắn với các loại tác vụ =====
# Mỗi loại task có vài từ khóa liên quan dùng để phân loại dòng nhập
KEYWORDS = {
    'install': ['cài', 'install', 'thiết lập', 'set up'],
    'config': ['cấu hình', 'config', 'thiết lập'],
    'write': ['viết', 'tạo', 'xây'],
    'test': ['test', 'kiểm'],
    'debug': ['debug', 'sửa', 'gỡi lỗi'],
    'plan': ['chia', 'phân', 'xây dựng kế hoạch'],
}

# ===== Hàm phụ: xác định loại task dựa vào dòng text =====
def classify_task(line):
    for k, vlist in KEYWORDS.items():
        for v in vlist:
            if v in line.lower():
                return k  # Nếu khớp từ khóa thì gán vào nhóm đó
    return 'misc'  # Nếu không khớp gì thì coi là "misc" (khác)

# ===== Hàm chính: phân rã đoạn văn thành các task nhỏ =====
def planbreak(text):
    # Chia đoạn input thành từng câu nhỏ theo dấu chấm, phẩy, xuống dòng
    lines = re.split(r'[.,;\n]', text)
    tasks = []
    for line in lines:
        line = line.strip()
        if len(line) < 4:  # bỏ qua câu quá ngắn
            continue
        task_type = classify_task(line)  # xác định loại task
        tasks.append((task_type, line))  # lưu task dạng tuple (loại, nội dung)
    return tasks

# ===== Xuất kết quả ra dạng checklist markdown =====
def print_tasks(tasks):
    print("# Task Breakdown:\n")
    for task_type, line in tasks:
        print(f"- [ ] ({task_type}) {line}")

# ===== Giao diện CLI: cho nhập từ stdin hoặc từ file =====
if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as f:
            input_text = f.read()  # nếu có truyền file, đọc nội dung
    else:
        print("Nhập một ý định (kết thúc bằng Ctrl+D):")
        input_text = sys.stdin.read()  # đọc input từ bàn phím

    tasks = planbreak(input_text)  # phân tích ý định thành task
    print_tasks(tasks)  # in ra kết quả



"""
# Hướng dẫn sử dụng planbreak.py

1. Chạy trực tiếp nhập từ bàn phím:
   python3 planbreak.py
   → Nhập ý định (text), kết thúc Ctrl+D
   → Nhận danh sách task dạng checklist markdown

2. Chạy với file đầu vào:
   python3 planbreak.py tenfile.txt
   → Đọc mục tiêu từ file, in ra task checklist

3. Mục đích:
   Chia mục tiêu/ý định thành các task nhỏ theo loại (install, write, test, debug...)

4. Output mẫu:
   - [ ] (write) Viết một parser đơn giản
   - [ ] (test) Test vài dòng code
   - [ ] (debug) Sửa lỗi nếu có

---

Dùng để tách ý định phức tạp thành bước khả thi trong CLI, chạy trên Python 3, máy RAM thấp.

"""