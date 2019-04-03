
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
        
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        pre = None
        current= head
        
        while current:
            current.random = Node(current.val, None, current.random)
            if pre:
                pre.random.next = current.random
            pre = current
            current = current.next
			
        current = head.random
        while current:
            if current.random:
                current.random = current.random.random
            current = current.next
        return head.random