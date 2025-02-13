
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: TreeNode) -> bool:
        return root.val == root.left.val + root.right.val


tree = TreeNode(10, TreeNode(8), TreeNode(2))
print(Solution().checkTree(tree))