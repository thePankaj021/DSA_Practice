class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = [0] * 26
        k = 0

        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1])) % 26 == 1:
                k += 1
            else:
                k = 1

            idx = ord(ch) - ord('a')
            dp[idx] = max(dp[idx], k)

        return sum(dp)