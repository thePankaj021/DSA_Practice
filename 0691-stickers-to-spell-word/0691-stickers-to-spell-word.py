from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_counts = [Counter(s) for s in stickers]

        @lru_cache(None)
        def dfs(remain):
            if not remain:
                return 0

            target_count = Counter(remain)
            ans = float('inf')

            for sticker in sticker_counts:
                if remain[0] not in sticker:
                    continue

                new_remain = []

                for ch, cnt in target_count.items():
                    if cnt > sticker[ch]:
                        new_remain.extend([ch] * (cnt - sticker[ch]))

                new_remain = ''.join(sorted(new_remain))

                res = dfs(new_remain)
                if res != -1:
                    ans = min(ans, 1 + res)

            return -1 if ans == float('inf') else ans

        return dfs(''.join(sorted(target)))