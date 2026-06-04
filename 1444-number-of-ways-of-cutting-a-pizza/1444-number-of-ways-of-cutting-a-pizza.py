from typing import List
from functools import lru_cache

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(pizza), len(pizza[0])

        pre = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                pre[r][c] = (
                    pre[r + 1][c]
                    + pre[r][c + 1]
                    - pre[r + 1][c + 1]
                    + (pizza[r][c] == 'A')
                )

        @lru_cache(None)
        def dfs(r, c, cuts):
            if pre[r][c] == 0:
                return 0
            if cuts == 1:
                return 1

            ans = 0

            for nr in range(r + 1, m):
                if pre[r][c] - pre[nr][c] > 0:
                    ans = (ans + dfs(nr, c, cuts - 1)) % MOD

            for nc in range(c + 1, n):
                if pre[r][c] - pre[r][nc] > 0:
                    ans = (ans + dfs(r, nc, cuts - 1)) % MOD

            return ans

        return dfs(0, 0, k)