class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        ans = 0

        for house in houses:
            idx = bisect.bisect_left(heaters, house)

            left = float('inf') if idx == 0 else house - heaters[idx - 1]
            right = float('inf') if idx == len(heaters) else heaters[idx] - house

            ans = max(ans, min(left, right))

        return ans