class Node(object):
    def __init__(self):
        self.children = dict()
        self.number = 0


class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root

        for letter in key:
            child = node.children.get(letter)
            if not child:
                child = Node()
                node.children[letter] = child
            node = child
            node.number += val

        return None

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if not node:
                return 0

        return node.number


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple", 3)
obj.sum("ap")
obj.insert("apple", 2)
obj.sum("ap")
