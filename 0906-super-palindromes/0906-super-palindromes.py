class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L = int(left)
        R = int(right)

        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]

        ans = 0
        limit = 100000

        for k in range(1, limit):
            s = str(k)

            # odd length palindrome
            p = int(s + s[-2::-1])
            sq = p * p

            if sq > R:
                break

            if sq >= L and is_palindrome(sq):
                ans += 1

        for k in range(1, limit):
            s = str(k)

            # even length palindrome
            p = int(s + s[::-1])
            sq = p * p

            if sq > R:
                break

            if sq >= L and is_palindrome(sq):
                ans += 1

        return ans