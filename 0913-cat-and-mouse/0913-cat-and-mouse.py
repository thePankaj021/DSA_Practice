from collections import deque
from typing import List

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)

        DRAW, MOUSE, CAT = 0, 1, 2

        color = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = len([x for x in graph[c] if x != 0])

        q = deque()

        for i in range(1, n):
            color[0][i][0] = MOUSE
            color[0][i][1] = MOUSE
            q.append((0, i, 0, MOUSE))
            q.append((0, i, 1, MOUSE))

            color[i][i][0] = CAT
            color[i][i][1] = CAT
            q.append((i, i, 0, CAT))
            q.append((i, i, 1, CAT))

        def parents(m, c, turn):
            if turn == 0:
                for pc in graph[c]:
                    if pc != 0:
                        yield m, pc, 1
            else:
                for pm in graph[m]:
                    yield pm, c, 0

        while q:
            m, c, turn, result = q.popleft()

            for pm, pc, pturn in parents(m, c, turn):
                if color[pm][pc][pturn] != DRAW:
                    continue

                if (pturn == 0 and result == MOUSE) or \
                   (pturn == 1 and result == CAT):

                    color[pm][pc][pturn] = result
                    q.append((pm, pc, pturn, result))

                else:
                    degree[pm][pc][pturn] -= 1

                    if degree[pm][pc][pturn] == 0:
                        loser = CAT if pturn == 0 else MOUSE
                        color[pm][pc][pturn] = loser
                        q.append((pm, pc, pturn, loser))

        return color[1][2][0]