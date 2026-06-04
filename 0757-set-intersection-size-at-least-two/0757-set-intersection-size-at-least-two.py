class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        a = b = -1
        ans = 0

        for start, end in intervals:
            if start > b:
                ans += 2
                a = end - 1
                b = end
            elif start > a:
                ans += 1
                a = b
                b = end

        return ans