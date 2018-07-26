class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        cur = self.getnthnode(index)
        if cur is None or cur.val is None:
            return -1

        return cur.val

    def getnthnode(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        cur = self.head
        i = 0
        while i < index and cur is not None:
            cur = cur.next
            i += 1

        return cur

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        head = ListNode(val)
        head.next = self.head
        self.head = head
        return self.head

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        tail = ListNode(val)
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = tail
        return self.head

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0:
            self.addAtHead(val)
            return

        prev = self.getnthnode(index - 1)
        if prev is None:
            return

        cur = ListNode(val)
        cur.next = prev.next

        prev.next = cur

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        cur = self.getnthnode(index)
        if cur is None:
            return

        prev = self.getnthnode(index - 1)
        nextnode = cur.next
        if prev is None:
            self.head = nextnode
        else:
            prev.next = nextnode


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.get(0)
obj.addAtIndex(1, 2)
obj.get(0)
obj.addAtIndex(0, 1)
obj.get(0)
obj.get(1)

obj.addAtHead(1)
obj.addAtTail(3)
obj.get(3)
obj.deleteAtIndex(1)
obj.get(1)
