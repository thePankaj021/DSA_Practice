from collections import deque

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque([(0, 0, 0, 0)])  # row, col, dir(0=H,1=V), moves
        seen = {(0, 0, 0)}

        while q:
            r, c, d, dist = q.popleft()

            if (r, c, d) == (n - 1, n - 2, 0):
                return dist

            if d == 0:
                if c + 2 < n and grid[r][c + 2] == 0:
                    state = (r, c + 1, 0)
                    if state not in seen:
                        seen.add(state)
                        q.append((r, c + 1, 0, dist + 1))

                if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                    state = (r + 1, c, 0)
                    if state not in seen:
                        seen.add(state)
                        q.append((r + 1, c, 0, dist + 1))

                    state = (r, c, 1)
                    if state not in seen:
                        seen.add(state)
                        q.append((r, c, 1, dist + 1))

            else:
                if r + 2 < n and grid[r + 2][c] == 0:
                    state = (r + 1, c, 1)
                    if state not in seen:
                        seen.add(state)
                        q.append((r + 1, c, 1, dist + 1))

                if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                    state = (r, c + 1, 1)
                    if state not in seen:
                        seen.add(state)
                        q.append((r, c + 1, 1, dist + 1))

                    state = (r, c, 0)
                    if state not in seen:
                        seen.add(state)
                        q.append((r, c, 0, dist + 1))

        return -1