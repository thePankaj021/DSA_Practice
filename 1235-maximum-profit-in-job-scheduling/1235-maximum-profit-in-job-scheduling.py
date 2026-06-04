from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [s for s, _, _ in jobs]

        n = len(jobs)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            s, e, p = jobs[i]
            j = bisect_left(starts, e)

            dp[i] = max(dp[i + 1], p + dp[j])

        return dp[0]