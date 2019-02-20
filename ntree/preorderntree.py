
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> '[int]':
        if not root:
            return []
        
        res = []
        stack = [root]
        while stack:
            tmpnode = stack.pop()
            res.append(tmpnode.val)
            stack.extend(reversed(tmpnode.children))
        
        return res





class RecursiveSolution:
    def preorder(self, root: 'Node') -> '[int]':
        if not root:
            return []
        
        res = [root.val]

        for child in root.children:
            res.extend(self.preorder(child))
    
        return res