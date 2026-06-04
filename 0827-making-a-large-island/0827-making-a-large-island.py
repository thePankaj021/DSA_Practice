from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2
        area = {0: 0}

        def dfs(r, c, idx):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0

            grid[r][c] = idx

            return (
                1
                + dfs(r + 1, c, idx)
                + dfs(r - 1, c, idx)
                + dfs(r, c + 1, idx)
                + dfs(r, c - 1, idx)
            )

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area[island_id] = dfs(r, c, island_id)
                    island_id += 1

        ans = max(area.values(), default=0)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    size = 1

                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < n and 0 <= nc < n:
                            idx = grid[nr][nc]

                            if idx not in seen:
                                seen.add(idx)
                                size += area.get(idx, 0)

                    ans = max(ans, size)

        return ans