class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7

        dp = [[[0] * 16 for _ in range(6)] for _ in range(n + 1)]

        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for last in range(6):
                for cnt in range(1, rollMax[last] + 1):
                    if dp[i - 1][last][cnt] == 0:
                        continue

                    for nxt in range(6):
                        if nxt == last:
                            if cnt + 1 <= rollMax[last]:
                                dp[i][nxt][cnt + 1] = (
                                    dp[i][nxt][cnt + 1] + dp[i - 1][last][cnt]
                                ) % MOD
                        else:
                            dp[i][nxt][1] = (
                                dp[i][nxt][1] + dp[i - 1][last][cnt]
                            ) % MOD

        ans = 0
        for j in range(6):
            for cnt in range(1, rollMax[j] + 1):
                ans = (ans + dp[n][j][cnt]) % MOD

        return ans