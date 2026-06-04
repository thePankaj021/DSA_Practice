from typing import List

class Solution:
    def profitableSchemes(
        self,
        n: int,
        minProfit: int,
        group: List[int],
        profit: List[int]
    ) -> int:

        MOD = 10**9 + 7

        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for g, p in zip(group, profit):
            new_dp = [row[:] for row in dp]

            for members in range(n - g + 1):
                for prof in range(minProfit + 1):
                    if dp[members][prof] == 0:
                        continue

                    new_members = members + g
                    new_profit = min(minProfit, prof + p)

                    new_dp[new_members][new_profit] = (
                        new_dp[new_members][new_profit]
                        + dp[members][prof]
                    ) % MOD

            dp = new_dp

        ans = 0
        for members in range(n + 1):
            ans = (ans + dp[members][minProfit]) % MOD

        return ans