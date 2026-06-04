class Solution:
    def pathSum(self, root, targetSum):
        res = []

        def dfs(node, total, path):
            if not node:
                return

            total += node.val
            path.append(node.val)

            if not node.left and not node.right:
                if total == targetSum:
                    res.append(path[:])
            else:
                dfs(node.left, total, path)
                dfs(node.right, total, path)

            path.pop()

        dfs(root, 0, [])
        return res