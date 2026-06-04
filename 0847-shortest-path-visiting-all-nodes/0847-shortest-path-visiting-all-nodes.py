from typing import List
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        target = (1 << n) - 1

        q = deque()
        visited = set()

        for i in range(n):
            mask = 1 << i
            q.append((i, mask, 0))
            visited.add((i, mask))

        while q:
            node, mask, dist = q.popleft()

            if mask == target:
                return dist

            for nei in graph[node]:
                new_mask = mask | (1 << nei)

                state = (nei, new_mask)

                if state not in visited:
                    visited.add(state)
                    q.append((nei, new_mask, dist + 1))