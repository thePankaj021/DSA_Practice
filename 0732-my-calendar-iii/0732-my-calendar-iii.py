from collections import defaultdict

class MyCalendarThree:

    def __init__(self):
        self.events = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.events[startTime] += 1
        self.events[endTime] -= 1

        active = 0
        max_active = 0

        for time in sorted(self.events):
            active += self.events[time]
            max_active = max(max_active, active)

        return max_active