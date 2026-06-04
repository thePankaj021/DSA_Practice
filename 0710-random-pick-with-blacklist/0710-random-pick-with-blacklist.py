from typing import List
import random

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.bound = n - len(blacklist)
        black = set(blacklist)

        self.mapping = {}
        last = n - 1

        for b in blacklist:
            if b < self.bound:
                while last in black:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self) -> int:
        x = random.randint(0, self.bound - 1)
        return self.mapping.get(x, x)