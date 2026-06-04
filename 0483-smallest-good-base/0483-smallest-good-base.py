class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)

        for m in range(n.bit_length(), 1, -1):
            k = int(n ** (1 / (m - 1)))

            if k <= 1:
                continue

            s = 1
            cur = 1

            for _ in range(m - 1):
                cur *= k
                s += cur

            if s == n:
                return str(k)

        return str(n - 1)