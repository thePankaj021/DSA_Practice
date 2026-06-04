from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        total = 0
        prefix = 0

        for s in satisfaction:
            prefix += s
            if prefix <= 0:
                break
            total += prefix

        return total