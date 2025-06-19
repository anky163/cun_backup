#!/usr/bin/env python3
# generate_variants.py - sinh biến thể cho trigger/response dùng từ đồng nghĩa

import argparse
import json
import random
import sys
from urllib.request import urlopen, Request
import socket
from urllib.error import URLError

# ===== Synonym dictionary =====
SYNONYM_MAP = {
    "mệt": ["kiệt sức", "đuối", "quá tải"],
    "vô nghĩa": ["trống rỗng", "vô vị", "chẳng còn gì đáng bám"],
    "đau": ["nhức nhối", "xé ruột", "sát thương tinh thần"],
    "chết": ["biến mất", "tắt", "shutdown"],
    "sống": ["tồn tại", "duy trì mạch", "giữ nhịp"],
    "không còn": ["mất hết", "biến mất sạch", "trôi đi"],
}

# ===== Helpers =====

def fetch_json_from_url(url):
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        print(f"[DEBUG] Fetching URL: {url}")
        with urlopen(req, timeout=10) as resp:
            raw = resp.read()
            print(f"[DEBUG] Fetched {len(raw)} bytes")
            text = raw.decode("utf-8")
            return json.loads(text)
    except socket.timeout:
        sys.exit("[ERROR] Connection timed out")
    except URLError as e:
        sys.exit(f"[ERROR] Failed to fetch URL: {e}")
    except json.JSONDecodeError as e:
        sys.exit(f"[ERROR] Invalid JSON: {e}")

def apply_synonym(text):
    for word, synonyms in SYNONYM_MAP.items():
        if word in text:
            return text.replace(word, random.choice(synonyms))
    return text  # fallback

def generate_variants(entry, count):
    variants = []
    for _ in range(count):
        trig = apply_synonym(entry["trigger"])
        resp = apply_synonym(entry["response"])
        if trig != entry["trigger"] or resp != entry["response"]:
            variants.append({"trigger": trig, "response": resp})
    return variants

def flatten_variants(data):
    flat = []
    for entry in data:
        flat.append(entry["original"])
        flat.extend(entry["variants"])
    return flat

# ===== Main =====
def main():
    parser = argparse.ArgumentParser(description="Generate variants of response rules")
    parser.add_argument("--url", help="URL to JSON input file")
    parser.add_argument("--input", default="response_rules.json", help="Path to input JSON file")
    parser.add_argument("--output", default="resp_bulk.json", help="Output JSON file path")
    parser.add_argument("--variants", type=int, default=3, help="Variants per entry")
    parser.add_argument("--dry-run", action="store_true", help="Print instead of write file")
    parser.add_argument("--flat", action="store_true", help="Flatten to list of dicts")
    args = parser.parse_args()

    # ===== Load input =====
    if args.url:
        data = fetch_json_from_url(args.url)
    else:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            sys.exit(f"[ERROR] Failed to load input: {e}")

    result = []
    for entry in data:
        variants = generate_variants(entry, args.variants)
        result.append({
            "original": entry,
            "variants": variants
        })

    output = flatten_variants(result) if args.flat else result

    if args.dry_run:
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        with open(args.output, "w", encoding="utf-8") as out:
            json.dump(output, out, ensure_ascii=False, indent=2)
        print(f"[+] Output written to {args.output}")

if __name__ == "__main__":
    main()
