from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        res = []
        q = deque([root])
        left_to_right = True

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()

                if left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)
            left_to_right = not left_to_right

        return res