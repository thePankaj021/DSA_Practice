from typing import List

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        copy = [row[:] for row in grid]
        for r, c in hits:
            if copy[r][c] == 1:
                copy[r][c] = 0

        parent = list(range(m * n + 1))
        size = [1] * (m * n + 1)
        roof = m * n

        def index(r, c):
            return r * n + c

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return

            parent[ry] = rx
            size[rx] += size[ry]

        def top_size():
            return size[find(roof)]

        for r in range(m):
            for c in range(n):
                if copy[r][c] == 1:
                    if r == 0:
                        union(index(r, c), roof)

                    if r > 0 and copy[r - 1][c] == 1:
                        union(index(r, c), index(r - 1, c))

                    if c > 0 and copy[r][c - 1] == 1:
                        union(index(r, c), index(r, c - 1))

        res = []

        for r, c in reversed(hits):
            if grid[r][c] == 0:
                res.append(0)
                continue

            prev = top_size()

            copy[r][c] = 1
            curr = index(r, c)

            if r == 0:
                union(curr, roof)

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and copy[nr][nc] == 1:
                    union(curr, index(nr, nc))

            now = top_size()
            res.append(max(0, now - prev - 1))

        return res[::-1]