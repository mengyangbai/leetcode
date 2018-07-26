class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serializeHelper(self, res, children):
        if len(children) == 0:
            return res

        tmpres = []
        for node in children:
            tmpres.append(node.val)
            tmpres = self.serializeHelper(tmpres, node.children)

        res.append(tmpres)
        return res

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: Node
        :rtype: str
        """
        if not root:
            return None

        res = []
        res.append(root.val)

        res = self.serializeHelper(res, root.children)

        return res

    def deserializeHelper(self, fatherNode, childrenData, index):
        if len(childrenData) == 0:
            return fatherNode
        while index < len(childrenData):
            if index == (len(childrenData) - 1) or type(
                    childrenData[index + 1]) == int:
                sunNode = Node(childrenData[index], [])
                fatherNode.children.append(sunNode)
                index += 1
            elif type(childrenData[index + 1]) == list:
                sunNode = Node(childrenData[index], [])
                sunNode = self.deserializeHelper(sunNode,
                                                 childrenData[index + 1], 0)
                fatherNode.children.append(sunNode)
                index = index + 2

        return fatherNode

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        fatherNode = Node(data[0], [])
        if len(data) == 1:
            fatherNode = self.deserializeHelper(fatherNode, data[1], 0)

        return fatherNode


# Your Codec object will be instantiated and called as such:
codec = Codec()
root5 = Node(44, [])
# root6 = Node(6, [])
# root2 = Node(2, [])
# root4 = Node(4, [])
# root3 = Node(3, [root5, root6])
# root1 = Node(1, [root3, root2, root4])

codec.deserialize(codec.serialize(root5))
