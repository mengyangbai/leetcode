# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        last=TreeNode(-1)
        qstack=[root]
        while qstack:
            node=qstack.pop()
            last.right=node
            last.left=None
            if node and node.right:
                qstack.append(node.right)
            if node and node.left:
                qstack.append(node.left)
            last=node