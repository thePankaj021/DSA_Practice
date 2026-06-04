class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(n):
            if p[j] == '*':
                dp[j + 1] = dp[j]

        for i in range(m):
            ndp = [False] * (n + 1)
            for j in range(n):
                if p[j] == '*':
                    ndp[j + 1] = ndp[j] or dp[j + 1]
                elif p[j] == '?' or s[i] == p[j]:
                    ndp[j + 1] = dp[j]
            dp = ndp

        return dp[n]