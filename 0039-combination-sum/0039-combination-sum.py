class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i == len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])  # reuse same number
            cur.pop()

            dfs(i + 1, cur, total)  # skip

        dfs(0, [], 0)
        return res