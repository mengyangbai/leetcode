"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> [[int]]:
        if not root:
            return []
        
        res =[]
        stack = [root]
        while stack:
            tmpres = []
            tmpstack = []
            for node in stack:
                tmpres.append(node.val)
                if node.children:
                    tmpstack.extend(node.children)

            res.append(tmpres)
            stack = tmpstack
        
        return res

'''

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> ret = new LinkedList<>();
        
        if (root == null) return ret;
        
        Queue<Node> queue = new LinkedList<>();
        
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            List<Integer> curLevel = new LinkedList<>();
            int len = queue.size();
            for (int i = 0; i < len; i++) {
                Node curr = queue.poll();
                curLevel.add(curr.val);
                for (Node c : curr.children)
                    queue.offer(c);
            }
            ret.add(curLevel);
        }
        
        return ret;        
    }
}

'''