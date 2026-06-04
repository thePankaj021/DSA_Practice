class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        n = len(nums)

        mid = (n + 1) // 2
        small = nums[:mid][::-1]
        large = nums[mid:][::-1]

        nums[::2] = small
        nums[1::2] = large