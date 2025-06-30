import time
import os

LOGFILE = os.environ.get("LOGFILE", "logs.md")

def add_log(content):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    entry = f"## {timestamp}\n\n{content.strip()}\n\n---\n"
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(entry)
    return timestamp

def grep_log(term):
    if not os.path.exists(LOGFILE):
        return []
    results = []
    with open(LOGFILE, "r", encoding="utf-8") as f:
        for line in f:
            if term.lower() in line.lower():
                results.append(line.strip())
    return results

def cat_log():
    if not os.path.exists(LOGFILE):
        return ""
    with open(LOGFILE, "r", encoding="utf-8") as f:
        return f.read()
