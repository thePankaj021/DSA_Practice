from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes):
        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0

            while l < r and boxes[l] == boxes[l + 1]:
                l += 1
                k += 1

            ans = (k + 1) ** 2 + dp(l + 1, r, 0)

            for m in range(l + 1, r + 1):
                if boxes[m] == boxes[l]:
                    ans = max(
                        ans,
                        dp(l + 1, m - 1, 0) +
                        dp(m, r, k + 1)
                    )

            return ans

        return dp(0, len(boxes) - 1, 0)