# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
        # return str(self.val) + str(self.left) + str(self.right)


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            node1 = self.flatten(root.left)
            node2 = self.flatten(root.right)
            root.left = None
            root.right = node1 if node1 else node2
            if node1:
                while node1.right:
                    node1 = node1.right
                node1.right = node2
            return root

        return None


def level_order(root: TreeNode):
    if not root:
        print([])

    queue = []
    queue.append(root)
    ret = []
    while queue:
        nodes, res = [], []
        while queue:
            nodes.append(queue.pop(0))

        for node in nodes:
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ret.append(res)

    return ret


if __name__ == "__main__":
    t = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)))
    print(level_order(Solution().flatten(t)))
