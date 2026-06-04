from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        graph = defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)

        q = deque([(0, 0)])
        visited = {0}

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            for nei in graph[arr[i]]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, steps + 1))

            graph[arr[i]].clear()

            if i + 1 < n and i + 1 not in visited:
                visited.add(i + 1)
                q.append((i + 1, steps + 1))

            if i - 1 >= 0 and i - 1 not in visited:
                visited.add(i - 1)
                q.append((i - 1, steps + 1))

        return -1