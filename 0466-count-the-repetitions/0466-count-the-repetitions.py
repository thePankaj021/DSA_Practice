class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        recall = {}
        s1cnt = s2cnt = index = 0

        while True:
            s1cnt += 1

            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2cnt += 1
                        index = 0

            if s1cnt == n1:
                return s2cnt // n2

            if index in recall:
                s1cnt_prime, s2cnt_prime = recall[index]
                pre_loop = (s1cnt_prime, s2cnt_prime)
                in_loop = (
                    s1cnt - s1cnt_prime,
                    s2cnt - s2cnt_prime
                )
                break
            else:
                recall[index] = (s1cnt, s2cnt)

        ans = pre_loop[1]

        remaining = n1 - pre_loop[0]

        ans += (remaining // in_loop[0]) * in_loop[1]

        rest = remaining % in_loop[0]

        index = list(recall.keys())[
            list(recall.values()).index(
                (pre_loop[0], pre_loop[1])
            )
        ]

        for _ in range(rest):
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        ans += 1
                        index = 0

        return ans // n2