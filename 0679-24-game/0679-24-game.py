from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            n = len(nums)

            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue

                    rest = []
                    for k in range(n):
                        if k != i and k != j:
                            rest.append(nums[k])

                    a, b = nums[i], nums[j]

                    for val in [a + b, a - b, a * b]:
                        if dfs(rest + [val]):
                            return True

                    if abs(b) > EPS:
                        if dfs(rest + [a / b]):
                            return True

            return False

        return dfs([float(x) for x in cards])