class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)

        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    m = min(len(words[i]), len(words[j]))
                    for k in range(m, -1, -1):
                        if words[i].endswith(words[j][:k]):
                            overlap[i][j] = k
                            break

        dp = [[""] * n for _ in range(1 << n)]

        for i in range(n):
            dp[1 << i][i] = words[i]

        for mask in range(1 << n):
            for last in range(n):
                if not dp[mask][last]:
                    continue

                for nxt in range(n):
                    if mask & (1 << nxt):
                        continue

                    new_mask = mask | (1 << nxt)
                    cand = dp[mask][last] + words[nxt][overlap[last][nxt]:]

                    if (not dp[new_mask][nxt] or
                        len(cand) < len(dp[new_mask][nxt]) or
                        (len(cand) == len(dp[new_mask][nxt]) and cand < dp[new_mask][nxt])):
                        dp[new_mask][nxt] = cand

        full = (1 << n) - 1
        ans = ""

        for s in dp[full]:
            if s and (not ans or len(s) < len(ans) or (len(s) == len(ans) and s < ans)):
                ans = s

        return ans