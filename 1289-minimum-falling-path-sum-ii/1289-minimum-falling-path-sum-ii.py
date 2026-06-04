class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for i in range(1, n):
            min1 = min2 = float('inf')
            idx1 = -1

            for j in range(n):
                val = grid[i - 1][j]
                if val < min1:
                    min2 = min1
                    min1 = val
                    idx1 = j
                elif val < min2:
                    min2 = val

            for j in range(n):
                grid[i][j] += min1 if j != idx1 else min2

        return min(grid[-1])