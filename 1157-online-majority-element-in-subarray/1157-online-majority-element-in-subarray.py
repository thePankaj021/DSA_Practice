from collections import defaultdict
from bisect import bisect_left, bisect_right
import random

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.pos = defaultdict(list)

        for i, x in enumerate(arr):
            self.pos[x].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            x = self.arr[random.randint(left, right)]
            idx = self.pos[x]

            freq = bisect_right(idx, right) - bisect_left(idx, left)

            if freq >= threshold:
                return x

        return -1