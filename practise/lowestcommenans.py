# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)

        x = root.val

        if q.val == x or p.val == x:
            return root

        if p.val <= x and q.val >= x:
            return root

        if q.val < x:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > x:
            return self.lowestCommonAncestor(root.right, p, q)


node2 = TreeNode(2)
node3 = TreeNode(3)
node2.right = node3

newnode2 = TreeNode(2)
newnode3 = TreeNode(3)

a = Solution()

a.lowestCommonAncestor(node2, newnode3, newnode2)
