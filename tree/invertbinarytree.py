# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        if root == None:
            return []
        if root.left or root.right:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            if root.left:
                root.left = self.invertTree(root.left)
            if root.right:
                root.right = self.invertTree(root.right)
        
        return root