"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root:
            head, _ = self.helper(root)
            return head
        return None


    def helper(self, root):
        """Idea: Construct a DLL for each subtree, then return the head and tail"""
        head, tail = root, root
        if root.left:
            lh, lt = self.helper(root.left)
            lt.right = root
            root.left = lt
            head = lh
        if root.right:
            rh, rt = self.helper(root.right)
            rh.left = root
            root.right = rh
            tail = rt
        head.left = tail
        tail.right = head
        return (head, tail)