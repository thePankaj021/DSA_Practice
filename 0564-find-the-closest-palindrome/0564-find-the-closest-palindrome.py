class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        l = len(n)

        candidates = {
            10 ** (l - 1) - 1,
            10 ** l + 1
        }

        prefix = int(n[:(l + 1) // 2])

        for x in (prefix - 1, prefix, prefix + 1):
            s = str(x)

            if l % 2:
                p = int(s + s[:-1][::-1])
            else:
                p = int(s + s[::-1])

            candidates.add(p)

        candidates.discard(num)

        return str(min(candidates,
                       key=lambda x: (abs(x - num), x)))