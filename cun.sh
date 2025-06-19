#!/bin/bash
# cun.sh – shell wrapper hệ Cún CLI
# Load config từ config.cfg → gọi module tương ứng

# === Load config ===
CONFIG="config.cfg"
declare -A CFG

if [ -f "$CONFIG" ]; then
  while IFS='=' read -r key val; do
    [[ "$key" =~ ^#.*$ || -z "$key" ]] && continue
    CFG["$key"]=$(echo "$val" | xargs)
  done < "$CONFIG"
fi

# === Extract paths/configs từ config.cfg ===
LOGFILE=${CFG[logfile]:-logs.md}
MEMFILE=${CFG[memfile]:-mem.json}
RESP_RULES=${CFG[resp_rules]:-resp_rules.txt}

CMD=$1
shift

case "$CMD" in
  planbreak)
    python3 planbreak.py "$@"
    ;;

  mem)
    MEMFILE="$MEMFILE" python3 memcore.py "$@"
    ;;

  resp)
    RESP_RULES="$RESP_RULES" python3 respgen.py "$@"
    ;;

  prompt)
    python3 prompt_engine.py "$@"
    ;;

  codegen)
    python3 codegen.py "$@"
    ;;

  log)
    LOGFILE="$LOGFILE" python3 mdlog.py "$@"
    ;;

  *)
    echo "Cún CLI - Lệnh hỗ trợ:"
    echo "  planbreak [file]        – chia task"
    echo "  mem add|get|grep|dump   – memory"
    echo "  resp [input]            – phản hồi"
    echo "  prompt save|gen         – template"
    echo "  codegen shell|py [desc] – sinh code"
    echo "  log add|grep|cat        – markdown log"
    ;;
esac
