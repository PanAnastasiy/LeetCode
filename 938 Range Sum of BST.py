
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(10,
                TreeNode(5,
                         TreeNode(3),
                         TreeNode(7)),
                TreeNode(15,
                         None,
                         TreeNode(18)))


class Solution(object):

    @staticmethod
    def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if low <= root.val <= high:
            return root.val + Solution.rangeSumBST(root.left, low, high) + Solution.rangeSumBST(root.right, low, high)
        else:
            return Solution.rangeSumBST(root.left, low, high) + Solution.rangeSumBST(root.right, low, high)




print(Solution.rangeSumBST(tree, 7, 15))
