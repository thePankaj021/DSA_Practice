from functools import lru_cache

class Solution:
    def racecar(self, target: int) -> int:

        @lru_cache(None)
        def dp(t):
            if t == 0:
                return 0

            n = t.bit_length()

            if (1 << n) - 1 == t:
                return n

            # Overshoot and reverse
            ans = n + 1 + dp((1 << n) - 1 - t)

            # Undershoot, reverse, then move forward
            for m in range(n - 1):
                distance = (1 << (n - 1)) - 1
                back = (1 << m) - 1

                ans = min(
                    ans,
                    (n - 1) + 1 + m + 1 +
                    dp(t - distance + back)
                )

            return ans

        return dp(target)