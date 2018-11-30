class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []

        def preorder(root):
            if not root:
                return
            ret.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ret

    def preorderTraversal2(self, root):
        """
                :type root: TreeNode
                :rtype: List[int]
                """

        ret = []
        s = []
        if root:
            s.append(root)

        while s:
            node = s.pop()
            ret.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)

        return ret


if __name__ == "__main__":
    head = TreeNode(1)
    head.right = TreeNode(2)
    head.right.left = TreeNode(3)
    print(Solution().preorderTraversal2(head))
