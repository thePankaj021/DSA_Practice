class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows = {}
        cols = {}
        diag1 = {}
        diag2 = {}
        active = set()

        for r, c in lamps:
            if (r, c) in active:
                continue

            active.add((r, c))
            rows[r] = rows.get(r, 0) + 1
            cols[c] = cols.get(c, 0) + 1
            diag1[r - c] = diag1.get(r - c, 0) + 1
            diag2[r + c] = diag2.get(r + c, 0) + 1

        ans = []

        for r, c in queries:
            if (rows.get(r, 0) > 0 or
                cols.get(c, 0) > 0 or
                diag1.get(r - c, 0) > 0 or
                diag2.get(r + c, 0) > 0):
                ans.append(1)
            else:
                ans.append(0)

            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc

                    if (nr, nc) in active:
                        active.remove((nr, nc))

                        rows[nr] -= 1
                        cols[nc] -= 1
                        diag1[nr - nc] -= 1
                        diag2[nr + nc] -= 1

        return ans
        