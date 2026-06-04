from collections import Counter
from functools import lru_cache

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        def clean(s):
            i = 0
            for j in range(len(s) + 1):
                if j == len(s) or s[j] != s[i]:
                    if j - i >= 3:
                        return clean(s[:i] + s[j:])
                    i = j
            return s

        @lru_cache(None)
        def dfs(board, hand_str):
            board = clean(board)

            if not board:
                return 0

            cnt = Counter(hand_str)
            ans = float('inf')

            for i in range(len(board) + 1):
                for c in cnt:
                    if cnt[c] == 0:
                        continue

                    if i > 0 and board[i - 1] == c:
                        continue

                    choose = (
                        (i < len(board) and board[i] == c) or
                        (0 < i < len(board) and board[i - 1] == board[i] != c)
                    )

                    if not choose:
                        continue

                    nxt_hand = list(hand_str)
                    nxt_hand.remove(c)

                    ans = min(
                        ans,
                        1 + dfs(board[:i] + c + board[i:],
                                ''.join(sorted(nxt_hand)))
                    )

            return ans

        res = dfs(board, ''.join(sorted(hand)))
        return -1 if res == float('inf') else res
        