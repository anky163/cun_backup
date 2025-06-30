# planbreak/plan_core.py

def load_tasks_from_file(path):
    """Đọc file văn bản và trả về danh sách các task đã strip."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def format_tasks(tasks):
    """Định dạng danh sách task thành chuỗi số thứ tự + nội dung."""
    lines = [f"{i+1:02d}. {task}" for i, task in enumerate(tasks)]
    return "\n".join(lines)
