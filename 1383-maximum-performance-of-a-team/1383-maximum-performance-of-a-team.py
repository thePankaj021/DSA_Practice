from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7

        engineers = sorted(zip(efficiency, speed), reverse=True)

        heap = []
        speed_sum = 0
        ans = 0

        for e, s in engineers:
            heapq.heappush(heap, s)
            speed_sum += s

            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)

            ans = max(ans, speed_sum * e)

        return ans % MOD