from collections import defaultdict
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        pos = defaultdict(list)

        for i, c in enumerate(ring):
            pos[c].append(i)

        n = len(ring)

        @lru_cache(None)
        def dp(i, cur):
            if i == len(key):
                return 0

            ans = float('inf')

            for nxt in pos[key[i]]:
                d = abs(nxt - cur)
                step = min(d, n - d)

                ans = min(ans, step + 1 + dp(i + 1, nxt))

            return ans

        return dp(0, 0)