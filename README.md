# Bộ CLI Cún Offline

Bộ tool tối giản để chạy local, không cần AI server, dành cho máy RAM thấp, CPU Ryzen5U.

---

## Module gồm

- `planbreak.py` : chia task từ câu goal input
- `memcore.py` : memory key-value CLI đơn giản (add/get/grep/dump)
- `respgen.py` : rule-based response generator kiểu Cún
- `cun.sh`     : bash wrapper gọi nhanh 3 module trên

---

## Cài đặt

1. Clone hoặc copy 4 file vào cùng thư mục

2. Cấp quyền cho cun.sh:

```bash
chmod +x cun.sh
