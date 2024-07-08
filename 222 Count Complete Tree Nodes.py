
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(3, TreeNode(4), TreeNode(5)))


class Solution(object):

    @staticmethod
    def countNodes(root: TreeNode) -> int:
        return 1 + Solution.countNodes(root.left) + Solution.countNodes(root.right) if root else 0


print(Solution.countNodes(tree))
