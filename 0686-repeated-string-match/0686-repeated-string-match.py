class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        s = a
        count = 1

        while len(s) < len(b):
            s += a
            count += 1

        if b in s:
            return count

        s += a
        if b in s:
            return count + 1

        return -1