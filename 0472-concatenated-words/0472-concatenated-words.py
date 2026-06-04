from functools import lru_cache

class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        wordset = set(words)

        @lru_cache(None)
        def can(word):
            for i in range(1, len(word)):
                left, right = word[:i], word[i:]

                if left in wordset and (right in wordset or can(right)):
                    return True
            return False

        res = []

        for word in words:
            wordset.remove(word)
            if can(word):
                res.append(word)
            wordset.add(word)

        return res