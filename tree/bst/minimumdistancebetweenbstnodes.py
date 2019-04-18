# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min = 2**31
        self.prev = 2**31

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            self.min = min(self.min, abs(self.prev-node.val))
            self.prev = node.val
            traverse(node.right)
        traverse(root)
        return self.min

'''
public class Solution {
    private Integer previousAccess = null;
    private int minDiff = Integer.MAX_VALUE;

    public int minDiffInBST(TreeNode root) {
        minDiff = Integer.MAX_VALUE;
        inOrder(root);
        return minDiff;

    }

    private void inOrder(TreeNode root) {
        if (root == null) {
            return;
        }
        inOrder(root.left);
        if (previousAccess != null) {
            int diff = root.val - previousAccess;
            if (diff < minDiff) {
                minDiff = diff;
            }
        }
        previousAccess = root.val;
        inOrder(root.right);
    }
}
'''