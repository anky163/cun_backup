#!/bin/bash
# auto_run_resp_gen.sh - Tự động fetch + sinh variant + cập nhật Trie
set -e

# ===== Cấu hình =====
VARIANT_SCRIPT="generate_variants.py"
RESPGEN_SCRIPT="respgen.py"
VARIANT_OUTPUT="resp_bulk.json"
RESP_RULES="resp_rules.json"
export RESP_RULES

# 🔗 Link raw JSON mày đã push lên GitHub
USE_URL="https://raw.githubusercontent.com/anky163/quy-t-c-ph-n-h-i-C-n-CLI-assistant/refs/heads/main/response_rules.json"

# ===== Bước 1: Fetch & sinh biến thể =====
echo "[1] 🔄 Fetch dữ liệu từ URL & sinh biến thể..."
python3 "$VARIANT_SCRIPT" \
  --url "$USE_URL" \
  --output "$VARIANT_OUTPUT" \
  --variants 3 \
  --flat

# ===== Bước 2: Nạp vào Trie qua respgen.py =====
echo "[2] 🧠 Nạp phản hồi vào Trie..."
jq -c '.[]' "$VARIANT_OUTPUT" | while read -r entry; do
  TRIG=$(echo "$entry" | jq -r '.trigger')
  RESP=$(echo "$entry" | jq -r '.response')

  echo "$TRIG" > .respgen_pending_prompt.txt
  echo "$RESP" | python3 "$RESPGEN_SCRIPT" > /dev/null
done

echo "✅ Xong. Đã cập nhật $RESP_RULES (Trie phản xạ)"
