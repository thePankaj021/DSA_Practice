from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1

        INF = float('inf')
        dp = [INF] * n

        maxd = 0
        for i in range(n):
            maxd = max(maxd, jobDifficulty[i])
            dp[i] = maxd

        for day in range(2, d + 1):
            ndp = [INF] * n

            for i in range(day - 1, n):
                hardest = 0

                for j in range(i, day - 2, -1):
                    hardest = max(hardest, jobDifficulty[j])

                    if dp[j - 1] != INF:
                        ndp[i] = min(ndp[i], dp[j - 1] + hardest)

            dp = ndp

        return dp[-1]