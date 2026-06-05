class Solution:
    def binaryTreePaths(self, root):
        if not root:return []
        if not root.left and not root.right:return [str(root.val)]
        return [str(root.val)+'->'+p for c in(root.left,root.right) if c for p in self.binaryTreePaths(c)]