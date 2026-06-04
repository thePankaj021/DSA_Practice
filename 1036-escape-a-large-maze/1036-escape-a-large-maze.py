class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(map(tuple, blocked))
        LIMIT = len(blocked) * (len(blocked) - 1) // 2

        def bfs(start, end):
            seen = {tuple(start)}
            q = [tuple(start)]

            while q and len(seen) <= LIMIT:
                x, y = q.pop()

                if [x, y] == end:
                    return True

                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < 10**6 and 0 <= ny < 10**6 and
                        (nx, ny) not in blocked and
                        (nx, ny) not in seen):
                        seen.add((nx, ny))
                        q.append((nx, ny))

            return len(seen) > LIMIT

        return bfs(source, target) and bfs(target, source)