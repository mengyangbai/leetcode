# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
        p = dummyNode
        q = head

        for x in range(m - 1):
            p.next = q
            q = q.next
            p = p.next

        start = None
        end = q
        next = None
        for x in range(m, n + 1):
            next = q.next
            q.next = start
            start = q
            q = next

        p.next = start
        end.next = next
        return dummyNode.next
        