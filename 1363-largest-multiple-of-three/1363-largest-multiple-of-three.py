from typing import List
from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        cnt = Counter(digits)
        total = sum(digits)

        mod1 = [1, 4, 7]
        mod2 = [2, 5, 8]

        def remove(nums, k):
            for _ in range(k):
                found = False
                for d in nums:
                    if cnt[d]:
                        cnt[d] -= 1
                        found = True
                        break
                if not found:
                    return False
            return True

        r = total % 3

        if r == 1:
            if not remove(mod1, 1):
                remove(mod2, 2)
        elif r == 2:
            if not remove(mod2, 1):
                remove(mod1, 2)

        res = []
        for d in range(9, -1, -1):
            res.extend([str(d)] * cnt[d])

        if not res:
            return ""

        if res[0] == '0':
            return "0"

        return "".join(res)