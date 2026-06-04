from typing import List
from math import sqrt

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        ans = 1

        for i in range(n):
            x1, y1 = darts[i]

            for j in range(i + 1, n):
                x2, y2 = darts[j]

                dx = x2 - x1
                dy = y2 - y1
                d = sqrt(dx * dx + dy * dy)

                if d > 2 * r:
                    continue

                mx = (x1 + x2) / 2
                my = (y1 + y2) / 2

                h = sqrt(r * r - (d / 2) ** 2)

                ux = -dy / d
                uy = dx / d

                for sign in (1, -1):
                    cx = mx + sign * h * ux
                    cy = my + sign * h * uy

                    count = 0
                    for x, y in darts:
                        if (x - cx) ** 2 + (y - cy) ** 2 <= r * r + 1e-7:
                            count += 1

                    ans = max(ans, count)

        return ans