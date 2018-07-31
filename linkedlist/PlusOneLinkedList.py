# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res, it = 0, head
        while it != None:
            res = res*10 + it.val
            it = it.next
        res += 1
        res_head = temp = ListNode(0)
        for ch in str(res):
            temp.next = ListNode(int(ch))
            temp = temp.next
        return res_head.next
