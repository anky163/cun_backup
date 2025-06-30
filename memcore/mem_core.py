import os
import json

MEMFILE = os.environ.get("MEMFILE", "mem.json")

def load_mem():
    if not os.path.exists(MEMFILE):
        return {}
    with open(MEMFILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return {}

def save_mem(data):
    with open(MEMFILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_mem(key, value):
    data = load_mem()
    if key in data:
        data[key] += "\n" + value
    else:
        data[key] = value
    save_mem(data)

def get_mem(key):
    data = load_mem()
    return data.get(key)

def grep_mem(term):
    data = load_mem()
    term_lower = term.lower()
    return {
        k: v for k, v in data.items()
        if term_lower in k.lower() or term_lower in v.lower()
    }

def dump_mem():
    return load_mem()
