from collections import deque

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque()
        self.max_len = max(map(len, words))

        for word in words:
            node = self.trie
            for ch in reversed(word):
                node = node.setdefault(ch, {})
            node['#'] = True

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        if len(self.stream) > self.max_len:
            self.stream.pop()

        node = self.trie

        for ch in self.stream:
            if ch not in node:
                return False
            node = node[ch]
            if '#' in node:
                return True

        return False