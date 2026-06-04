class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        dp = [1] * (n + 1)

        for i in range(n):
            ndp = [0] * (n + 1)

            if s[i] == 'I':
                prefix = 0
                for j in range(n - i):
                    prefix = (prefix + dp[j]) % MOD
                    ndp[j] = prefix
            else:
                suffix = 0
                for j in range(n - i - 1, -1, -1):
                    suffix = (suffix + dp[j + 1]) % MOD
                    ndp[j] = suffix

            dp = ndp

        return dp[0]