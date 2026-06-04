class Solution:
    def uniqueLetterString(self, s: str) -> int:
        pos = {}

        for i, ch in enumerate(s):
            if ch not in pos:
                pos[ch] = [-1]

            pos[ch].append(i)

        n = len(s)
        ans = 0

        for ch in pos:
            pos[ch].append(n)

            arr = pos[ch]

            for i in range(1, len(arr) - 1):
                ans += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])

        return ans