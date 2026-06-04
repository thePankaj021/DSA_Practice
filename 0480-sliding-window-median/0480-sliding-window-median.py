from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums, k):
        window = SortedList(nums[:k])
        res = []

        for i in range(k, len(nums) + 1):
            if k % 2:
                res.append(float(window[k // 2]))
            else:
                res.append((window[k // 2 - 1] + window[k // 2]) / 2)

            if i == len(nums):
                break

            window.remove(nums[i - k])
            window.add(nums[i])

        return res