from bisect import bisect_left, bisect_right

class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        new_intervals = []
        i = 0
        n = len(self.intervals)

        while i < n and self.intervals[i][1] < left:
            new_intervals.append(self.intervals[i])
            i += 1

        while i < n and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i += 1

        new_intervals.append([left, right])

        while i < n:
            new_intervals.append(self.intervals[i])
            i += 1

        self.intervals = new_intervals

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect_right(self.intervals, [left, float('inf')]) - 1
        return i >= 0 and self.intervals[i][0] <= left and right <= self.intervals[i][1]

    def removeRange(self, left: int, right: int) -> None:
        new_intervals = []

        for start, end in self.intervals:
            if end <= left or start >= right:
                new_intervals.append([start, end])
            else:
                if start < left:
                    new_intervals.append([start, left])
                if end > right:
                    new_intervals.append([right, end])

        self.intervals = new_intervals