class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def dfs(i, path):
            if len(path) == 4:
                if i == len(s):
                    res.append('.'.join(path))
                return

            for j in range(i, min(i + 3, len(s))):
                part = s[i:j + 1]

                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue

                path.append(part)
                dfs(j + 1, path)
                path.pop()

        dfs(0, [])
        return res