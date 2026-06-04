from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Sum of every window of size k
        window = [0] * (n - k + 1)
        cur = sum(nums[:k])
        window[0] = cur

        for i in range(1, n - k + 1):
            cur += nums[i + k - 1] - nums[i - 1]
            window[i] = cur

        m = len(window)

        left = [0] * m
        best = 0
        for i in range(m):
            if window[i] > window[best]:
                best = i
            left[i] = best

        right = [0] * m
        best = m - 1
        for i in range(m - 1, -1, -1):
            if window[i] >= window[best]:
                best = i
            right[i] = best

        ans = [-1, -1, -1]
        max_sum = 0

        for mid in range(k, m - k):
            l = left[mid - k]
            r = right[mid + k]

            total = window[l] + window[mid] + window[r]

            if total > max_sum:
                max_sum = total
                ans = [l, mid, r]

        return ans