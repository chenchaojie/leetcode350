# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def subIsSymmetric(left, right):
            if not left and not right:
                return True
            if left and right and left.val == right.val:
                return subIsSymmetric(left.right, right.left) and subIsSymmetric(left.left, right.right)
            else:
                return False

        if not root:
            return True
        return subIsSymmetric(root.left, root.right)


if __name__ == "__main__":
    pass
