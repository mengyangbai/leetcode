import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.count = 0
        while head:
            self.count += 1
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        ran = random.randint(0, self.count - 1)
        node = self.head
        while ran:
            ran -= 1
            node = node.next
        
        return node.val

        