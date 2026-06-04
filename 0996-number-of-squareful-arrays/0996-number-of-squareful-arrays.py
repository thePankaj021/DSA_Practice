from collections import Counter

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        count = Counter(nums)
        graph = {x: [] for x in count}

        for x in count:
            for y in count:
                r = int((x + y) ** 0.5)
                if r * r == x + y:
                    graph[x].append(y)

        n = len(nums)

        def dfs(x, remain):
            count[x] -= 1

            if remain == 0:
                res = 1
            else:
                res = 0
                for y in graph[x]:
                    if count[y]:
                        res += dfs(y, remain - 1)

            count[x] += 1
            return res

        ans = 0
        for x in count:
            ans += dfs(x, n - 1)

        return ans