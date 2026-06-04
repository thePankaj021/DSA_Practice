from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))

        cand1 = None
        cand2 = None

        for u, v in edges:
            if parent[v] != v:
                cand1 = [parent[v], v]
                cand2 = [u, v]
                break
            parent[v] = u

        def find(x):
            while uf[x] != x:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            uf[pb] = pa
            return True

        uf = list(range(n + 1))

        for u, v in edges:
            if cand2 and [u, v] == cand2:
                continue

            if not union(u, v):
                if cand1:
                    return cand1
                return [u, v]

        if cand2:
            return cand2