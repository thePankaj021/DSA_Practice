from collections import deque

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)

        def reachable(start, end, box_pos):
            q = deque([start])
            seen = {start}

            while q:
                x, y = q.popleft()
                if (x, y) == end:
                    return True

                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < m and 0 <= ny < n and
                        grid[nx][ny] != '#' and
                        (nx, ny) != box_pos and
                        (nx, ny) not in seen):
                        seen.add((nx, ny))
                        q.append((nx, ny))

            return False

        dq = deque([(0, box[0], box[1], player[0], player[1])])
        seen = {(box[0], box[1], player[0], player[1])}

        while dq:
            pushes, bx, by, px, py = dq.popleft()

            if (bx, by) == target:
                return pushes

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nbx, nby = bx + dx, by + dy
                needx, needy = bx - dx, by - dy

                if not (0 <= nbx < m and 0 <= nby < n and
                        0 <= needx < m and 0 <= needy < n):
                    continue

                if grid[nbx][nby] == '#' or grid[needx][needy] == '#':
                    continue

                if not reachable((px, py), (needx, needy), (bx, by)):
                    continue

                state = (nbx, nby, bx, by)

                if state not in seen:
                    seen.add(state)
                    dq.append((pushes + 1, nbx, nby, bx, by))

        return -1