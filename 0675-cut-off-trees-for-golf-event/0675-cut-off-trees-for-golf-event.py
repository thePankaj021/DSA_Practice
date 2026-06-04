from collections import deque
from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])

        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))

        trees.sort()

        def bfs(sr, sc, tr, tc):
            if sr == tr and sc == tc:
                return 0

            q = deque([(sr, sc, 0)])
            visited = {(sr, sc)}

            while q:
                r, c, d = q.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and 0 <= nc < n and
                        forest[nr][nc] != 0 and
                        (nr, nc) not in visited):

                        if nr == tr and nc == tc:
                            return d + 1

                        visited.add((nr, nc))
                        q.append((nr, nc, d + 1))

            return -1

        sr = sc = 0
        ans = 0

        for _, tr, tc in trees:
            dist = bfs(sr, sc, tr, tc)

            if dist == -1:
                return -1

            ans += dist
            sr, sc = tr, tc

        return ans