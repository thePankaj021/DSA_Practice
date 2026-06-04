class Solution:
    def sortedListToBST(self, head):
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        def build(l, r):
            if l > r:
                return None

            m = (l + r) // 2
            root = TreeNode(nums[m])

            root.left = build(l, m - 1)
            root.right = build(m + 1, r)

            return root

        return build(0, len(nums) - 1)