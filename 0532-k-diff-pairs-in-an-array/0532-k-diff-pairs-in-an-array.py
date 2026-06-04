class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        if k < 0:
            return 0

        from collections import Counter
        count = Counter(nums)
        res = 0

        for x in count:
            if k == 0:
                if count[x] > 1:
                    res += 1
            else:
                if x + k in count:
                    res += 1

        return res