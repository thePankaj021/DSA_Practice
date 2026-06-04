class Solution:
    def majorityElement(self, nums):
        c1 = c2 = None
        v1 = v2 = 0

        for x in nums:
            if x == c1:
                v1 += 1
            elif x == c2:
                v2 += 1
            elif v1 == 0:
                c1, v1 = x, 1
            elif v2 == 0:
                c2, v2 = x, 1
            else:
                v1 -= 1
                v2 -= 1

        return [x for x in (c1, c2) if nums.count(x) > len(nums) // 3]