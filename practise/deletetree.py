# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getsuccess(self, cur):
        while cur and cur.left:
            cur = cur.left
        return cur

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            p = self.getsuccess(root.right)
            root.val = p.val
            root.right = self.deleteNode(root.right, p.val)
            return root

        return root


node2 = TreeNode(2)
node4 = TreeNode(4)
node7 = TreeNode(7)
node3 = TreeNode(3)
node6 = TreeNode(6)
node5 = TreeNode(5)

node5.left = node3
node5.right = node6
node6.right = node7
node3.left = node2
node3.right = node4

a = Solution()

a.deleteNode(node5, 3)