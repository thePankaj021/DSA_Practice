class Solution:
    def findMode(self, root):
        from collections import defaultdict

        freq = defaultdict(int)

        def dfs(node):
            if not node:
                return
            freq[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_freq = max(freq.values())
        return [key for key, value in freq.items() if value == max_freq]