from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()
        ans = 0

        for i in range(len(nums)):
            if q and q[0] <= i - k:
                q.popleft()

            curr = nums[i]
            if len(q) % 2:
                curr ^= 1

            if curr == 0:
                if i + k > len(nums):
                    return -1
                q.append(i)
                ans += 1

        return ans