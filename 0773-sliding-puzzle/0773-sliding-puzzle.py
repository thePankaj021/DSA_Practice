from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(map(str, board[0] + board[1]))
        target = "123450"

        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        q = deque([(start, 0)])
        seen = {start}

        while q:
            state, steps = q.popleft()

            if state == target:
                return steps

            zero = state.index('0')

            for nxt in neighbors[zero]:
                s = list(state)
                s[zero], s[nxt] = s[nxt], s[zero]
                ns = ''.join(s)

                if ns not in seen:
                    seen.add(ns)
                    q.append((ns, steps + 1))

        return -1