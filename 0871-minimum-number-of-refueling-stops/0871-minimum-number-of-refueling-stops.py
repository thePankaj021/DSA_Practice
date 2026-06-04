from typing import List
import heapq

class Solution:
    def minRefuelStops(
        self,
        target: int,
        startFuel: int,
        stations: List[List[int]]
    ) -> int:

        max_heap = []
        fuel = startFuel
        prev = 0
        stops = 0

        stations.append([target, 0])

        for pos, gas in stations:
            fuel -= pos - prev

            while fuel < 0 and max_heap:
                fuel += -heapq.heappop(max_heap)
                stops += 1

            if fuel < 0:
                return -1

            heapq.heappush(max_heap, -gas)
            prev = pos

        return stops