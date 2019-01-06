# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findLeaves(self, root):
        ans = []
        def helper(root):
            l = 0
            if root.left:
                l = max(l, 1+helper(root.left))
            if root.right:
                l = max(l, 1+helper(root.right))
            if l == len(ans):
                ans.append([root.val])
            else:
                ans[l].append(root.val)
            return l
            
        if root:
            helper(root)
        return ans

        
