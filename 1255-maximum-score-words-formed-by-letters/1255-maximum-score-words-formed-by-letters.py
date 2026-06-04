from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        available = Counter(letters)
        n = len(words)

        word_cnt = [Counter(w) for w in words]
        word_score = [
            sum(score[ord(c) - ord('a')] for c in w)
            for w in words
        ]

        def dfs(i):
            if i == n:
                return 0

            ans = dfs(i + 1)

            if all(word_cnt[i][c] <= available[c] for c in word_cnt[i]):
                for c in word_cnt[i]:
                    available[c] -= word_cnt[i][c]

                ans = max(ans, word_score[i] + dfs(i + 1))

                for c in word_cnt[i]:
                    available[c] += word_cnt[i][c]

            return ans

        return dfs(0)