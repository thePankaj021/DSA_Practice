from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)
            dup = 1

            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx == 0 and dy == 0:
                    dup += 1
                    continue

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slopes[(dx, dy)] += 1

            cur = dup
            for cnt in slopes.values():
                cur = max(cur, cnt + dup)

            ans = max(ans, cur)

        return ans