class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        res = 0

        while True:
            visited = set()
            regions = []
            frontiers = []
            walls = []

            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and (r, c) not in visited:
                        region = []
                        frontier = set()
                        wall = 0
                        stack = [(r, c)]
                        visited.add((r, c))

                        while stack:
                            x, y = stack.pop()
                            region.append((x, y))

                            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                                nx, ny = x + dx, y + dy

                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 1 and (nx, ny) not in visited:
                                        visited.add((nx, ny))
                                        stack.append((nx, ny))
                                    elif isInfected[nx][ny] == 0:
                                        frontier.add((nx, ny))
                                        wall += 1

                        regions.append(region)
                        frontiers.append(frontier)
                        walls.append(wall)

            if not regions:
                break

            idx = max(range(len(frontiers)), key=lambda i: len(frontiers[i]))

            if len(frontiers[idx]) == 0:
                break

            res += walls[idx]

            for i, region in enumerate(regions):
                if i == idx:
                    for x, y in region:
                        isInfected[x][y] = -1
                else:
                    for x, y in frontiers[i]:
                        isInfected[x][y] = 1

        return res