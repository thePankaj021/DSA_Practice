from typing import List
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = deque()
        dp = [0] * len(nums)

        for i in range(len(nums)):
            dp[i] = nums[i] + max(0, dp[dq[0]] if dq else 0)

            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            dq.append(i)

            if dq[0] <= i - k:
                dq.popleft()

        return max(dp)