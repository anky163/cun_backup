# trie.py - Trie đơn giản hỗ trợ phản xạ đa hồi đáp (multi-response)

import random
import re

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = []  # Luôn lưu dưới dạng list để hỗ trợ multiple responses

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, value):
        key = self.clean(key)  # ⚠️ fix lỗi space/thừa
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        if isinstance(node.value, list):
            if value not in node.value:
                node.value.append(value)
        else:
            node.value = [value]

    def get(self, key):
        key = self.clean(key)  # đồng nhất với insert
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            node = node.children[char]
        if isinstance(node.value, list):
            return node.value
        return [node.value] if node.value else None

    def contains(self, key):
        return self.get(key) is not None

    def to_dict(self, node=None):
        node = node or self.root
        result = {"_": node.value} if node.value else {}
        for char, child in node.children.items():
            result[char] = self.to_dict(child)
        return result

    def from_dict(self, data):
        def _load(node, d):
            for char, sub in d.items():
                if char == "_":
                    node.value = sub if isinstance(sub, list) else [sub]
                else:
                    child = TrieNode()
                    node.children[char] = child
                    _load(child, sub)
        if data:
            _load(self.root, data)

    @staticmethod
    def clean(text):
        text = text.strip()
        text = re.sub(r"\s+", " ", text)
        return text.lower()
    
    def dump_all_prompts(self):
        results = []

        def dfs(node, path):
            if node.value:
                full_prompt = ''.join(path)
                results.append((full_prompt, node.value))
            for char, child in node.children.items():
                dfs(child, path + [char])

        dfs(self.root, [])
        return results

