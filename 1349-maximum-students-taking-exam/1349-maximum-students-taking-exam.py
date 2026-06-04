from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])

        valid_masks = []
        for r in range(m):
            avail = 0
            for c in range(n):
                if seats[r][c] == '.':
                    avail |= (1 << c)

            row_masks = []
            for mask in range(1 << n):
                if (mask & ~avail) == 0 and (mask & (mask << 1)) == 0:
                    row_masks.append(mask)
            valid_masks.append(row_masks)

        dp = {0: 0}

        for r in range(m):
            ndp = {}
            for mask in valid_masks[r]:
                students = bin(mask).count('1')

                for prev in dp:
                    if (mask & (prev << 1)) == 0 and (mask & (prev >> 1)) == 0:
                        ndp[mask] = max(
                            ndp.get(mask, 0),
                            dp[prev] + students
                        )

            dp = ndp

        return max(dp.values(), default=0)