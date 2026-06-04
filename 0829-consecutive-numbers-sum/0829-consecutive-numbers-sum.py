class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        k = 1

        while k * (k - 1) // 2 < n:
            remaining = n - k * (k - 1) // 2

            if remaining % k == 0:
                ans += 1

            k += 1

        return ans