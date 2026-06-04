from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        nums.sort()

        dp = [set() for _ in range(n + 1)]
        dp[0].add(0)

        for num in nums:
            for k in range(n - 1, -1, -1):
                for s in dp[k]:
                    dp[k + 1].add(s + num)

        for k in range(1, n // 2 + 1):
            if (total * k) % n == 0:
                target = (total * k) // n
                if target in dp[k]:
                    return True

        return False