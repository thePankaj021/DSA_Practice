from typing import List

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)

        total = sum(abs(nums[i] - nums[i - 1]) for i in range(1, n))
        ans = total

        for i in range(1, n):
            ans = max(
                ans,
                total - abs(nums[i] - nums[i - 1]) + abs(nums[i] - nums[0])
            )
            ans = max(
                ans,
                total - abs(nums[i] - nums[i - 1]) + abs(nums[i - 1] - nums[-1])
            )

        low = float('inf')
        high = float('-inf')

        for i in range(1, n):
            a, b = nums[i - 1], nums[i]
            low = min(low, max(a, b))
            high = max(high, min(a, b))

        ans = max(ans, total + 2 * (high - low))

        return ans