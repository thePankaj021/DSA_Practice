from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        intervals = []
        res = []
        max_height = 0

        for left, size in positions:
            right = left + size
            height = size

            for l, r, h in intervals:
                if l < right and left < r:  # overlap
                    height = max(height, h + size)

            intervals.append((left, right, height))
            max_height = max(max_height, height)
            res.append(max_height)

        return res