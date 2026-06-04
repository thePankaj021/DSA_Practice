class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):

                a, b = num[:i], num[i:j]

                if (a[0] == '0' and len(a) > 1) or \
                   (b[0] == '0' and len(b) > 1):
                    continue

                x, y = int(a), int(b)
                k = j

                while k < n:
                    z = str(x + y)

                    if not num.startswith(z, k):
                        break

                    k += len(z)
                    x, y = y, x + y

                if k == n:
                    return True

        return False