from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(1, n):
                matrix[r][c] += matrix[r][c - 1]

        ans = 0

        for left in range(n):
            for right in range(left, n):
                count = defaultdict(int)
                count[0] = 1
                curr = 0

                for r in range(m):
                    curr += matrix[r][right] - (matrix[r][left - 1] if left else 0)
                    ans += count[curr - target]
                    count[curr] += 1

        return ans