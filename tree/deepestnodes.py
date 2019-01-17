# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def depth(self, root):
        if not root:
            return 0
        
        return max(self.depth(root.left)+1,self.depth(root.right)+1)

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        left = self.depth(root.left)

        right = self.depth(root.right)

        if left == right:
            return root
        
        elif left < right:
            return self.subtreeWithAllDeepest(root.right)
        
        else:
            return self.subtreeWithAllDeepest(root.left)
