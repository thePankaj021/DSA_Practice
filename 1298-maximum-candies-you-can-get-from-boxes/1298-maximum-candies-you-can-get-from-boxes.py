from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int],
                   keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:

        owned = set(initialBoxes)
        have_keys = set()
        opened = set()
        q = deque(initialBoxes)

        total = 0

        while q:
            box = q.popleft()

            if box in opened:
                continue

            if status[box] == 1 or box in have_keys:
                opened.add(box)
                total += candies[box]

                for key in keys[box]:
                    if key not in have_keys:
                        have_keys.add(key)
                        if key in owned:
                            q.append(key)

                for b in containedBoxes[box]:
                    owned.add(b)
                    q.append(b)

        changed = True
        while changed:
            changed = False
            for box in list(owned):
                if box not in opened and (status[box] == 1 or box in have_keys):
                    q.append(box)
                    changed = True

            while q:
                box = q.popleft()

                if box in opened:
                    continue

                if status[box] == 1 or box in have_keys:
                    opened.add(box)
                    total += candies[box]

                    for key in keys[box]:
                        if key not in have_keys:
                            have_keys.add(key)
                            if key in owned:
                                q.append(key)

                    for b in containedBoxes[box]:
                        if b not in owned:
                            owned.add(b)
                        q.append(b)

        return total