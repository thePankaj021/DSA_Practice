class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))

        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i < 0:
            return -1

        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]

        digits[i + 1:] = reversed(digits[i + 1:])

        ans = int("".join(digits))

        return ans if ans < 2**31 else -1