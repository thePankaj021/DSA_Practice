from functools import cache

class Solution:
    def diffWaysToCompute(self, expression: str):
        @cache
        def dfs(expr):
            res = []

            for i, ch in enumerate(expr):
                if ch in '+-*':
                    left = dfs(expr[:i])
                    right = dfs(expr[i + 1:])

                    for a in left:
                        for b in right:
                            if ch == '+':
                                res.append(a + b)
                            elif ch == '-':
                                res.append(a - b)
                            else:
                                res.append(a * b)

            if not res:
                res.append(int(expr))

            return res

        return dfs(expression)