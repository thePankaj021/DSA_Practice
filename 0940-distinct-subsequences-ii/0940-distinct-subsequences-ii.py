class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 1
        last = {}

        for ch in s:
            new_dp = (dp * 2) % MOD
            if ch in last:
                new_dp = (new_dp - last[ch]) % MOD
            last[ch] = dp
            dp = new_dp

        return (dp - 1) % MOD