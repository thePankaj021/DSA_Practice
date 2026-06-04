from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        n = len(s1)

        def neighbors(s):
            i = 0
            while s[i] == s2[i]:
                i += 1

            res = []

            for j in range(i + 1, n):
                if s[j] == s2[i] and s[j] != s2[j]:
                    arr = list(s)
                    arr[i], arr[j] = arr[j], arr[i]
                    res.append("".join(arr))

            return res

        q = deque([(s1, 0)])
        visited = {s1}

        while q:
            cur, steps = q.popleft()

            if cur == s2:
                return steps

            for nxt in neighbors(cur):
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))