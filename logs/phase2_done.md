# Phase 2 — Cún CLI Assistant: Phản xạ học sâu & sinh biến thể (hoàn tất)

## 🧠 Mục tiêu:
- Tạo hệ phản xạ tự học bằng CLI
- Nhớ phản hồi từ người dùng
- Sinh biến thể trigger để hỗ trợ đa dạng nhập liệu
- Đồng bộ dữ liệu từ GitHub

## ✅ Module & chức năng:

### 📁 respgen/
- `respgen.py`: phản xạ từ Trie (học được, trả lời nhanh)
- `generate_variants.py`: sinh câu hỏi biến thể từ synonym
- `trie.py`: cấu trúc cây Trie
- `resp_rules.json`: bộ nhớ Trie (nội bộ)
- `resp_bulk.json`: danh sách biến thể sinh ra
- `auto_run_resp_gen.sh`: pipeline fetch → sinh → nạp

### 📁 data/ (trên GitHub)
- `response_rules.json`: rule gốc để generate, học

## 🔄 Luồng phản xạ:

GitHub JSON (response_rules.json)
↓
generate_variants.py
↓
resp_bulk.json
↓
respgen.py (Trie học)
↓
resp_rules.json
↓
Giao tiếp CLI / GUI


## 🧪 Đã test:
- Tương thích Unicode (🇻🇳🇰🇷 OK)
- Tự học phản hồi người dùng
- Sinh biến thể có logic
- Tự động hóa 1 dòng lệnh
- Kéo dữ liệu từ GitHub thành công
- Cấu trúc folder sạch

## todo: 
- codegen.py chưa có folder
- chỉnh sửa gui_cun.py để liên lạc với toàn bộ các chức năng

## ⚙ Tiếp theo (Phase 3, nếu có):
- Nâng cấp GUI (`gui_cun.py`)
- Export Trie → readable format
- Hệ tag/theme cho câu trả lời
- Học theo context dài

---

🧭 Ký hiệu hoàn tất: `Phase2_OK.`
