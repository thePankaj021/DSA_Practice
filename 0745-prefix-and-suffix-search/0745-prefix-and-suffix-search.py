class WordFilter:

    def __init__(self, words: List[str]):
        self.lookup = {}

        for idx, word in enumerate(words):
            n = len(word)
            for i in range(n + 1):
                prefix = word[:i]
                for j in range(n + 1):
                    suffix = word[j:]
                    self.lookup[(prefix, suffix)] = idx

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get((pref, suff), -1)