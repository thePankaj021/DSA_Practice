from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(
        self,
        routes: List[List[int]],
        source: int,
        target: int
    ) -> int:

        if source == target:
            return 0

        stop_to_routes = defaultdict(list)

        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        q = deque([(source, 0)])
        visited_stops = {source}
        visited_routes = set()

        while q:
            stop, buses = q.popleft()

            if stop == target:
                return buses

            for route_idx in stop_to_routes[stop]:
                if route_idx in visited_routes:
                    continue

                visited_routes.add(route_idx)

                for next_stop in routes[route_idx]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        q.append((next_stop, buses + 1))

        return -1