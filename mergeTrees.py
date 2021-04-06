# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is not None:
            self.taraverseTree(t1, t2)
            return t1
        else:
            self.taraverseTree(t2, t1)
            return t2

    def taraverseTree(self, t1: TreeNode, t2: TreeNode):
        if t1 is not None and t2 is not None:
            t1.val = t1.val + t2.val
        else:
            return

        if t1.left is None and t2.left is not None:
            t1.left = TreeNode(0)
        if t1.right is None and t2.right is not None:
            t1.right = TreeNode(0)

        self.taraverseTree(t1.left, t2.left)
        self.taraverseTree(t1.right, t2.right)
