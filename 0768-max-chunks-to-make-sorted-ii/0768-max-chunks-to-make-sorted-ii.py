class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []

        for num in arr:
            cur_max = num

            while stack and stack[-1] > num:
                cur_max = max(cur_max, stack.pop())

            stack.append(cur_max)

        return len(stack)