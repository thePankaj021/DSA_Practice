class Solution:
    MOD = 10**9 + 7

    def assignEdgeWeights(self, edges, queries):
        n = len(edges) + 1
        LOG = (n).bit_length()

        # Build tree
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Binary Lifting
        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        def dfs(node, par):
            parent[0][node] = par
            for nei in graph[node]:
                if nei != par:
                    depth[nei] = depth[node] + 1
                    dfs(nei, node)

        dfs(1, 0)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                parent[k][v] = parent[k - 1][parent[k - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % self.MOD

        ans = []

        for u, v in queries:
            w = lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[w]

            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow2[dist - 1])

        return ans