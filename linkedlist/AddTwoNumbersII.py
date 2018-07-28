# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        answer = None
        carry = 0
        while stack1 and stack2:
            add = stack1.pop() + stack2.pop() + carry
            carry = 1 if add >= 10 else 0
            temp = answer
            answer = ListNode(add % 10)
            answer.next = temp
        l = stack1 if stack1 else stack2
        while l:
            add = l.pop() + carry
            carry = 1 if add >= 10 else 0
            temp = answer
            answer = ListNode(add % 10)
            answer.next = temp
        if carry:
            temp = answer
            answer = ListNode(1)
            answer.next = temp
        return answer