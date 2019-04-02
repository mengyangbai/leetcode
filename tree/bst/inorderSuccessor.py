"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        while node.parent and node.parent.val < node.val:
            node = node.parent
        return node.parent
        

'''
class Solution {
    public Node inorderSuccessor(Node x) {
        if (x.right == null) {
            Node result = x.parent;
            while (result != null && result.val < x.val) {
                result = result.parent;
            }
            return result;
        } else {
            Node result = x.right;
            while (result.left != null) {
                result = result.left;
            }
            return result;
        }
    }
}
'''