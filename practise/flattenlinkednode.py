"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        nextnode = head.next
        cur = head

        if cur.child:
            cur.next = self.flatten(cur.child)
            cur.next.prev = cur
            cur.child = None
            while cur.next:
                cur = cur.next

        if nextnode:
            cur.next = self.flatten(nextnode)
            cur.next.prev = cur

        return head
