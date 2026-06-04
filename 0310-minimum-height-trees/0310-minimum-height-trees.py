from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        leaves = deque(i for i in range(n) if degree[i] == 1)
        remaining = n

        while remaining > 2:
            size = len(leaves)
            remaining -= size

            for _ in range(size):
                leaf = leaves.popleft()
                for nei in graph[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaves.append(nei)

        return list(leaves)