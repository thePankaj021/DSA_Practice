from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        maxReach = [0] * (n + 1)

        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            maxReach[left] = max(maxReach[left], right)

        taps = 0
        curr_end = 0
        farthest = 0

        for i in range(n):
            farthest = max(farthest, maxReach[i])

            if i == curr_end:
                if farthest <= i:
                    return -1
                taps += 1
                curr_end = farthest

        return taps