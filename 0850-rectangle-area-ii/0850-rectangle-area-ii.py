from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7

        events = []
        ys = set()

        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))
            ys.add(y1)
            ys.add(y2)

        events.sort()
        ys = sorted(ys)

        y_index = {y: i for i, y in enumerate(ys)}

        count = [0] * (len(ys) - 1)

        def covered_length():
            total = 0
            for i in range(len(count)):
                if count[i] > 0:
                    total += ys[i + 1] - ys[i]
            return total

        prev_x = events[0][0]
        area = 0

        for x, typ, y1, y2 in events:
            area += covered_length() * (x - prev_x)

            for i in range(y_index[y1], y_index[y2]):
                count[i] += typ

            prev_x = x

        return area % MOD