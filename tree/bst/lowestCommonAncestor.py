# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None

        if root.val == p or root == q:
            return root

        leftroot = self.lowestCommonAncestor(root.left, p, q)
        rightroot = self.lowestCommonAncestor(root.right, p, q)

        if leftroot and rightroot:
            return root

        if leftroot is not None:
            return leftroot
        else:
            return rightroot
'''
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root==null){
            return null;
        }
        if(root.val == p.val|| root.val == q.val){
            return root;
        }
        TreeNode leftroot = lowestCommonAncestor(root.left,p,q);
        TreeNode rightroot = lowestCommonAncestor(root.right,p,q);
        
        if(leftroot!=null && rightroot!=null){
            return root;
        }
        if(leftroot != null){
            return leftroot;
        }
        else{
            return rightroot;
        }            
    }
}
'''

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def stringToInt(input):
    return int(input)


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line)
            line = next(lines)
            m = stringToInt(line)
            line = next(lines)
            n = stringToInt(line)

            ret = Solution().lowestCommonAncestor(root, m, n)

            out = treeNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
