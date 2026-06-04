from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        m = len(s)
        d = len(digits)

        ans = 0

        # Numbers with fewer digits than n
        for length in range(1, m):
            ans += d ** length

        # Numbers with same length as n
        for i in range(m):
            smaller = 0

            for digit in digits:
                if digit < s[i]:
                    smaller += 1

            ans += smaller * (d ** (m - i - 1))

            if s[i] not in digits:
                return ans

        return ans + 1