class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, not_rob)

            left = dfs(node.left)
            right = dfs(node.right)

            rob_node = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)

            return (rob_node, not_rob)

        return max(dfs(root))