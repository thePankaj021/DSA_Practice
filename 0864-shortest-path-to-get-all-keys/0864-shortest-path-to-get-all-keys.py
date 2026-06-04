from typing import List
from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])

        keys = 0

        for r in range(m):
            for c in range(n):
                ch = grid[r][c]

                if ch == '@':
                    sr, sc = r, c
                elif 'a' <= ch <= 'f':
                    keys = max(keys, ord(ch) - ord('a') + 1)

        target_mask = (1 << keys) - 1

        q = deque([(sr, sc, 0, 0)])  # row, col, keymask, steps
        visited = {(sr, sc, 0)}

        while q:
            r, c, mask, steps = q.popleft()

            if mask == target_mask:
                return steps

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                cell = grid[nr][nc]

                if cell == '#':
                    continue

                new_mask = mask

                if 'a' <= cell <= 'f':
                    new_mask |= 1 << (ord(cell) - ord('a'))

                if 'A' <= cell <= 'F':
                    if not (mask & (1 << (ord(cell) - ord('A')))):
                        continue

                state = (nr, nc, new_mask)

                if state not in visited:
                    visited.add(state)
                    q.append((nr, nc, new_mask, steps + 1))

        return -1