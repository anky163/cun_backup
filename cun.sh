#!/bin/bash

# === Cấu hình biến môi trường ===
export PYTHONPATH="$PYTHONPATH:$(pwd)/planbreak:$(pwd)/respgen:$(pwd)/memcore:$(pwd)/promptgen:$(pwd)/codegen:$(pwd)/logs"

# === Lệnh gọi GUI ===
if [[ "$1" == "gui" ]]; then
  python3 gui/gui_cun.py
  exit 0
fi

# === CLI tiện ích ===
case "$1" in
  mem)
    shift
    python3 memcore/main.py "$@"
    ;;
  plan)
    shift
    python3 planbreak/main.py "$@"
    ;;
  prompt)
    shift
    python3 promptgen/main.py "$@"
    ;;
  code)
    shift
    python3 codegen/main.py "$@"
    ;;
  log)
    shift
    python3 logs/main.py "$@"
    ;;
  resp)
    shift
    python3 respgen/main.py "$@"
    ;;
  *)
    echo "❗ Lệnh không hợp lệ. Dùng:"
    echo "  ./cun.sh gui                       # Mở giao diện"
    echo "  ./cun.sh mem add/get/grep/dump ...  # Quản lý memory"
    echo "  ./cun.sh plan <taskfile.txt>        # Chia task"
    echo "  ./cun.sh prompt save/gen ...        # Template prompt"
    echo "  ./cun.sh code shell/py \"desc\"      # Sinh code"
    echo "  ./cun.sh log add/grep/cat ...       # Ghi log"
    echo "  ./cun.sh resp                       # Hỏi đáp CLI"
    ;;
esac
