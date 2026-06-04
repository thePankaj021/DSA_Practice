import random
from bisect import bisect_left

class Solution:

    def __init__(self, rects):
        self.rects = rects
        self.prefix = []
        self.total = 0

        for x1, y1, x2, y2 in rects:
            # number of integer points in rectangle
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            self.total += area
            self.prefix.append(self.total)

    def pick(self):
        # pick a random point index
        target = random.randint(1, self.total)

        # find rectangle
        idx = bisect_left(self.prefix, target)
        x1, y1, x2, y2 = self.rects[idx]

        # pick random point inside
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)

        return [x, y]