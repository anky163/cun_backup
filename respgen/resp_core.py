# resp_core.py
import os
import json
import random
from trie import Trie

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RULES_FILE = os.path.join(BASE_DIR, "resp_rules.json")

def load_trie(path=RULES_FILE):
    trie = Trie()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            trie.from_dict(data)
    return trie

def save_trie(trie, path=RULES_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(trie.to_dict(), f, ensure_ascii=False, indent=2)

def get_response(trigger):
    trie = load_trie()
    responses = trie.get(trigger.strip())
    if responses:
        return random.choice(responses)
    return None

def learn_response(trigger, response):
    trie = load_trie()
    trie.insert(trigger.strip(), response.strip())
    save_trie(trie)
    return True
