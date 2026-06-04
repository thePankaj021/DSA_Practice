class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []

        def build(l, r):
            if l > r:
                return [None]

            res = []
            for root in range(l, r + 1):
                lefts = build(l, root - 1)
                rights = build(root + 1, r)

                for left in lefts:
                    for right in rights:
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        res.append(node)

            return res

        return build(1, n)