class Solution:
    def searchRange(self, nums, target):
        def left():
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l

        def right():
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m
            return l

        l = left()
        if l == len(nums) or nums[l] != target:
            return [-1, -1]

        return [l, right() - 1]