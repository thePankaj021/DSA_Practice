class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]