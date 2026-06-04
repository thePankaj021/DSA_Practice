from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def count_pairs(dist):
            count = 0
            left = 0

            for right in range(n):
                while nums[right] - nums[left] > dist:
                    left += 1
                count += right - left

            return count

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            if count_pairs(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left