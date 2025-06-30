# fetch_raw_dump.py - tải response rules từ URL và dump dạng prefix trie vào resp_rules.json

import json
import requests
from trie import Trie  # đảm bảo trie.py nằm cùng thư mục

URL = "https://raw.githubusercontent.com/anky163/quy-t-c-ph-n-h-i-C-n-CLI-assistant/refs/heads/main/response_rules.json"
OUTFILE = "resp_rules.json"

def clean(text):
    return text.strip().replace("\n", " ").replace("\t", " ").strip()

def fetch_and_save_trie(url, outpath):
    print(f"[⇣] Tải từ: {url}")
    res = requests.get(url)
    res.raise_for_status()
    data = res.json()
    print(f"[✔] Tải thành công: {len(data)} dòng")

    trie = Trie()
    added = 0
    for item in data:
        trigger = clean(item.get("trigger", ""))
        response = clean(item.get("response", ""))
        if trigger and response:
            trie.insert(trigger, response)
            added += 1

    trie_dict = trie.to_dict()
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(trie_dict, f, ensure_ascii=False, indent=2)

    print(f"[💾] Đã lưu {added} trigger → response vào {outpath} dưới dạng trie")

if __name__ == "__main__":
    fetch_and_save_trie(URL, OUTFILE)
