from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        pq = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            time, r, c = heapq.heappop(pq)

            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and 0 <= nc < n and
                    (nr, nc) not in visited):

                    visited.add((nr, nc))
                    heapq.heappush(
                        pq,
                        (max(time, grid[nr][nc]), nr, nc)
                    )