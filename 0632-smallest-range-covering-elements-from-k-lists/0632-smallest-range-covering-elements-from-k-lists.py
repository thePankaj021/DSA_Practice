import heapq

class Solution:
    def smallestRange(self, nums):
        heap = []
        mx = float('-inf')

        for i, row in enumerate(nums):
            heap.append((row[0], i, 0))
            mx = max(mx, row[0])

        heapq.heapify(heap)

        start, end = -10**5, 10**5

        while True:
            mn, r, c = heapq.heappop(heap)

            if mx - mn < end - start:
                start, end = mn, mx

            if c + 1 == len(nums[r]):
                break

            nxt = nums[r][c + 1]
            mx = max(mx, nxt)

            heapq.heappush(heap, (nxt, r, c + 1))

        return [start, end]