class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        target = list(target)
        res = []
        stars = 0

        def can_replace(pos):
            changed = False
            for i in range(m):
                if target[pos + i] == '*':
                    continue
                if target[pos + i] != stamp[i]:
                    return False
                changed = True
            return changed

        def do_replace(pos):
            cnt = 0
            for i in range(m):
                if target[pos + i] != '*':
                    target[pos + i] = '*'
                    cnt += 1
            return cnt

        visited = [False] * (n - m + 1)

        while stars < n:
            done = False

            for i in range(n - m + 1):
                if not visited[i] and can_replace(i):
                    stars += do_replace(i)
                    visited[i] = True
                    done = True
                    res.append(i)

                    if stars == n:
                        break

            if not done:
                return []

        return res[::-1]