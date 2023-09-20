class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data)
        if self.head is None:
            node.next = self.head
            self.head = node
            self.head.next = node
            return
        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next
        ptr.next = node
        node.next = self.head
        self.head = node

    def show(self):
        if self.head is None:
            print("List is Empty")
        ptr = self.head
        for i in range(self.get_length()):
            print(ptr.data, end="-->")
            ptr = ptr.next

    def get_length(self):
        if self.head is None:
            print("List is Empty")
        ptr = self.head
        count = 0
        while ptr.next != self.head:
            count += 1
            ptr = ptr.next
        return count+1


ll = CircularLinkedList()
ll.insert_at_start(1)
ll.insert_at_start(2)
ll.insert_at_start(3)
ll.insert_at_start(4)
ll.insert_at_start(5)
ll.insert_at_start(6)
print(ll.get_length())
ll.show()
