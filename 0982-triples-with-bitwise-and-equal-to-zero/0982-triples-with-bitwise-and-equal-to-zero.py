class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        cnt = [0] * (1 << 16)

        for a in nums:
            for b in nums:
                cnt[a & b] += 1

        ans = 0

        for x in nums:
            mask = ((1 << 16) - 1) ^ x
            sub = mask

            while sub:
                ans += cnt[sub]
                sub = (sub - 1) & mask

            ans += cnt[0]

        return ans