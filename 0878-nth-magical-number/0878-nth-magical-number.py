class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        lcm = a * b // gcd(a, b)

        def count(x):
            return x // a + x // b - x // lcm

        left, right = 1, n * min(a, b)

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= n:
                right = mid
            else:
                left = mid + 1

        return left % MOD