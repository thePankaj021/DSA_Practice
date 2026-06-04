from typing import List
from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n
        ans = [0] * n

        def postorder(node, parent):
            for nei in graph[node]:
                if nei == parent:
                    continue

                postorder(nei, node)
                count[node] += count[nei]
                ans[node] += ans[nei] + count[nei]

        def preorder(node, parent):
            for nei in graph[node]:
                if nei == parent:
                    continue

                ans[nei] = ans[node] - count[nei] + (n - count[nei])
                preorder(nei, node)

        postorder(0, -1)
        preorder(0, -1)

        return ans