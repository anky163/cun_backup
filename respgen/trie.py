# trie.py - Trie đơn giản hỗ trợ phản xạ đa hồi đáp (multi-response)

import random

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = []  # Luôn lưu dưới dạng list để hỗ trợ multiple responses

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, value):
        node = self.root
        for char in key.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        if isinstance(node.value, list):
            if value not in node.value:
                node.value.append(value)
        else:
            node.value = [value]

    def get(self, key):
        node = self.root
        for char in key.lower():
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
