# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # 解法1层次遍历很简单
    # 解法深度遍历复杂点
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        if root.left and not root.right:
            return self.minDepth(root.left) + 1

        if root.right and not root.left:
            return self.minDepth(root.right) + 1

        return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)


if __name__ == "__main__":
    # t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    t = TreeNode(3, TreeNode(9))
    print(Solution().minDepth(t))
