# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.count = 0
    
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        _, covered = self.putCamera(root)
        if not covered:
            return self.count+1
        else:
            return self.count
    
    def putCamera(self, root):
        # Return: hasCamera(Bool) : Camera has been put at node n , isCovered(bool): node has been monitored
        if not root:
            return False, True
        
        leftHasCamera, leftCovered = self.putCamera(root.left)
        rightHasCamera, rightCovered = self.putCamera(root.right)
        
        
        covered = False
        if leftHasCamera or rightHasCamera:
            covered = True
        
        hasCamera = False
        if not rightCovered or not leftCovered:
            self.count += 1 # put camera at current node
            hasCamera = True
            covered = True
        
        return hasCamera, covered


'''
class Solution {
    public int minCameraCover(TreeNode root) {
        if(root == null ) return 0;
        int val = helper(root);

        // Handle the root NOT being made visible by a camera
        // in which case we have to manually do that.
        return val + (root.val == 0 ? 1 : 0);
    }

    public int helper(TreeNode root){
        if(root == null) return 0;

        int leftCameras = helper(root.left);
        int rightCameras = helper(root.right);
	
		// if at least one child is NOT null and NOT visible(2) then we must mark this node as camera.
        if((root.left != null && root.left.val == 0) || (root.right != null && root.right.val == 0)){
            root.val = 1;
        }
		// Check if one of the children are cameras in order to mark the current node as visible(2)
		else if((root.left != null && root.left.val == 1) || (root.right != null && root.right.val == 1)){
            root.val = 2;
        }

        return leftCameras + rightCameras + (root.val == 1 ? 1 : 0);
    }
}
'''