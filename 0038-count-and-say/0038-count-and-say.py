class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            cur = []
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                cur.append(str(j - i))
                cur.append(s[i])
                i = j
            s = ''.join(cur)

        return s