from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        dp = [[(-1, 0) for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1] = (0, 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] in "XS":
                    continue

                best_score = -1
                ways = 0

                for ni, nj in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if 0 <= ni < n and 0 <= nj < n:
                        score, cnt = dp[ni][nj]
                        if score > best_score:
                            best_score = score
                            ways = cnt
                        elif score == best_score:
                            ways = (ways + cnt) % MOD

                if best_score == -1:
                    continue

                val = 0 if board[i][j] == 'E' else int(board[i][j])
                dp[i][j] = (best_score + val, ways)

        score, ways = dp[0][0]
        return [0, 0] if score == -1 else [score, ways]