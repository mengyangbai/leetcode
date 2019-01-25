# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        leftdummy = ListNode(0)
        rightdummy = ListNode(0)
        rightcurrent = rightdummy
        leftcurrent = leftdummy

        if not head:
            return []
        

        while head:
            if head.val < x:
                leftcurrent.next = head
                leftcurrent = leftcurrent.next
            else:
                rightcurrent.next = head
                rightcurrent = rightcurrent.next
            
            head = head.next
        
        leftcurrent.next = rightdummy.next
        rightcurrent.next = None
        
        return leftdummy.next

a = Solution()
node1 = ListNode(1)
node4 = ListNode(4)
node3 = ListNode(3)
node2 = ListNode(2)
node5 = ListNode(5)
node22 = ListNode(2)
node1.next = node4
node4.next = node3
node3.next = node2
node2.next = node5
node5.next = node22

a.partition(node1,3)