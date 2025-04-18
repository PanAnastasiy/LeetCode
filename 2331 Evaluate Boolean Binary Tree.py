from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return bool(root.val)
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 3:
            return left and right
        elif root.val == 2:
            return left or right


print(Solution().evaluateTree(tree))
