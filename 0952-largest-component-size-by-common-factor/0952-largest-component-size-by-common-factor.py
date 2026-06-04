class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if size[pa] < size[pb]:
                pa, pb = pb, pa
            parent[pb] = pa
            size[pa] += size[pb]

        factor_map = {}

        for i, num in enumerate(nums):
            x = num
            d = 2
            factors = set()

            while d * d <= x:
                if x % d == 0:
                    factors.add(d)
                    while x % d == 0:
                        x //= d
                d += 1

            if x > 1:
                factors.add(x)

            for f in factors:
                if f in factor_map:
                    union(i, factor_map[f])
                else:
                    factor_map[f] = i

        return max(size[find(i)] for i in range(n))