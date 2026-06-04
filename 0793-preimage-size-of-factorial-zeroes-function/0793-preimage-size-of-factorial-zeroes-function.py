class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailing_zeroes(n):
            count = 0
            while n:
                n //= 5
                count += n
            return count

        def first_ge(target):
            left, right = 0, 5 * (target + 1)

            while left < right:
                mid = (left + right) // 2

                if trailing_zeroes(mid) >= target:
                    right = mid
                else:
                    left = mid + 1

            return left

        return first_ge(k + 1) - first_ge(k)