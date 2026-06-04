from functools import lru_cache

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @lru_cache(None)
        def dfs(t):
            if t == 0:
                return 0
            if t < x:
                return min(2 * t - 1, 2 * (x - t))

            p = x
            k = 0
            while p < t:
                p *= x
                k += 1

            if p == t:
                return k

            res = dfs(t - p // x) + k

            if p - t < t:
                res = min(res, dfs(p - t) + k + 1)

            return res

        return dfs(target)