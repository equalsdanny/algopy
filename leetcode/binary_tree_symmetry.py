# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.compare(root.left, root.right)

    def compare(self, left: TreeNode, right: TreeNode) -> bool:
        nones = sum([left is None, right is None])

        if nones == 1:
            return False
        elif nones == 2:
            return True

        if left.val != right.val:
            return False

        return self.compare(left.left, right.right) and \
               self.compare(left.right, right.left)
