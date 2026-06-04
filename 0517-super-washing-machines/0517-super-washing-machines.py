class Solution:
    def findMinMoves(self, machines):
        total = sum(machines)
        n = len(machines)

        if total % n:
            return -1

        avg = total // n
        ans = balance = 0

        for x in machines:
            balance += x - avg
            ans = max(ans, abs(balance), x - avg)

        return ans