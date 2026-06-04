class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            ndp = [0] * (k + 1)
            prefix = 0

            for j in range(k + 1):
                prefix += dp[j]

                if j >= i:
                    prefix -= dp[j - i]

                ndp[j] = prefix % MOD

            dp = ndp

        return dp[k]