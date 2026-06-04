class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(x):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(x // i, n)
            return cnt

        left, right = 1, m * n

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left