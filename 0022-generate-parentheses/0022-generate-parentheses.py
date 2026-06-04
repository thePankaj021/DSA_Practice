class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def dfs(s, open_cnt, close_cnt):
            if len(s) == 2 * n:
                res.append(s)
                return

            if open_cnt < n:
                dfs(s + "(", open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                dfs(s + ")", open_cnt, close_cnt + 1)

        dfs("", 0, 0)
        return res