class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 1

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 2 or right == 2:
                self.ans += 1
                return 0

            if left == 0 or right == 0:
                return 1

            return 2

        if dfs(root) == 2:
            self.ans += 1

        return self.ans