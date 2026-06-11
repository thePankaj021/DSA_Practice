from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = {}

        for row in wall:
            pos = 0
            for brick in row[:-1]:  # exclude last edge
                pos += brick
                edges[pos] = edges.get(pos, 0) + 1

        max_edges = max(edges.values(), default=0)
        return len(wall) - max_edges