from typing import List
from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        dq = deque([(0, 0)])

        while dq:
            x, y = dq.popleft()

            for d, (dx, dy) in enumerate(dirs, 1):
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    cost = dist[x][y] + (grid[x][y] != d)

                    if cost < dist[nx][ny]:
                        dist[nx][ny] = cost

                        if grid[x][y] == d:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))

        return dist[m - 1][n - 1]