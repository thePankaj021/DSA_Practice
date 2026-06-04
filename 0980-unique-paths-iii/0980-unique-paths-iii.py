class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        empty = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empty += 1
                elif grid[i][j] == 1:
                    sx, sy = i, j

        def dfs(x, y, remain):
            if grid[x][y] == 2:
                return 1 if remain == 0 else 0

            temp = grid[x][y]
            grid[x][y] = -1
            ans = 0

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    ans += dfs(nx, ny, remain - 1)

            grid[x][y] = temp
            return ans

        return dfs(sx, sy, empty)