
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        swap = [None, None]
        self.prev = TreeNode(float('-inf'))
        def dfs(node):
            if node:
                dfs(node.left)
                if node.val < self.prev.val:
                    if not swap[0]: swap[0] = self.prev
                    swap[1] = node
                self.prev = node
                dfs(node.right)
        dfs(root)
        swap[0].val, swap[1].val = swap[1].val, swap[0].val