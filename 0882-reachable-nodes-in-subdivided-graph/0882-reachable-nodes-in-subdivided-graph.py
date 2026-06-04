from typing import List
from collections import defaultdict
import heapq

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(list)

        for u, v, cnt in edges:
            graph[u].append((v, cnt + 1))
            graph[v].append((u, cnt + 1))

        dist = {0: 0}
        pq = [(0, 0)]

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for nei, weight in graph[node]:
                nd = d + weight

                if nd < dist.get(nei, float('inf')):
                    dist[nei] = nd
                    heapq.heappush(pq, (nd, nei))

        ans = sum(d <= maxMoves for d in dist.values())

        for u, v, cnt in edges:
            a = max(0, maxMoves - dist.get(u, float('inf')))
            b = max(0, maxMoves - dist.get(v, float('inf')))

            ans += min(cnt, a + b)

        return ans