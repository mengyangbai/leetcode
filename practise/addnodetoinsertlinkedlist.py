"""
# Definition for a Node.
"""


class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            node = Node(insertVal, None)
            node.next = node
            return node

        cur = head
        while cur and cur.next:
            if cur.val < cur.next.val:
                if cur.val <= insertVal and insertVal <= cur.next.val:
                    node = Node(insertVal, cur.next)
                    cur.next = node
                    break

            elif cur.val > cur.next.val:
                if insertVal >= cur.val or insertVal <= cur.next.val:
                    node = Node(insertVal, cur.next)
                    cur.next = node
                    break

            else:
                if cur.next == head:
                    node = Node(insertVal, cur.next)
                    cur.next = node
                    break

            cur = cur.next

        return head


node1 = Node(1, None)
node2 = Node(2, None)
node3 = Node(3, None)

node2 = node1.next
node3 = node2.next
node1 = node3.next

a = Solution()

a.insert(node1, 0)
