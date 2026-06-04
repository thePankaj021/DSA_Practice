from typing import List

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        nums.sort()

        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = 0

        for i in range(n):
            ans += nums[i] * (pow2[i] - pow2[n - 1 - i])

        return ans % MOD