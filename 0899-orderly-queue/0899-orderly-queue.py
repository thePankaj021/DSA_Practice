class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))

        ans = s

        for i in range(1, len(s)):
            candidate = s[i:] + s[:i]
            if candidate < ans:
                ans = candidate

        return ans