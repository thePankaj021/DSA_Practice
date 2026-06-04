class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}

        for r in rods:
            cur = dp.copy()

            for diff, h in cur.items():
                dp[diff + r] = max(dp.get(diff + r, 0), h)

                new_diff = abs(diff - r)
                dp[new_diff] = max(
                    dp.get(new_diff, 0),
                    h + min(diff, r)
                )

        return dp[0]