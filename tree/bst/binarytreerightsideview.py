# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: 'TreeNode') -> '[int]':
        res = []
        if not root:
            return res
        levelstack = [root]
        while levelstack:
            res.append(levelstack[0].val)
            tmpstack=[]
            for node in levelstack:
                if node.right:
                    tmpstack.append(node.right)
                if node.left:
                    tmpstack.append(node.left)

            levelstack = tmpstack

        return res
        