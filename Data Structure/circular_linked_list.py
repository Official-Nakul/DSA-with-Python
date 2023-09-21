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

    def insert_at_last(self, data):
        if self.head is None:
            self.insert_at_start(data)
            return
        ptr = self.head
        node = Node(data)
        while ptr.next != self.head:
            ptr = ptr.next
        ptr.next = node
        node.next = self.head

    def remove(self, inx):
        if self.head is None:
            return
        if inx == 0:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = ptr.next.next
            self.head = self.head.next
            return
        if inx == self.get_length() - 1:
            ptr = self.head
            count = 0
            while ptr:
                if count == inx - 1:
                    ptr.next = self.head
                    return
                count += 1
                ptr = ptr.next
        ptr = self.head
        count = 0
        while ptr:
            if count == inx - 1:
                ptr.next = ptr.next.next
                return
            count += 1
            ptr = ptr.next

    def show(self):
        if self.head is None:
            print("List is Empty")
        ptr = self.head
        for i in range(self.get_length()):
            print(ptr.data, end="-->")
            ptr = ptr.next
        print("Pointing to head")

    def get_length(self):
        if self.head is None:
            print("List is Empty")
        ptr = self.head
        count = 0
        while ptr.next != self.head:
            count += 1
            ptr = ptr.next
        return count + 1


ll = CircularLinkedList()
ll.insert_at_start(5)
ll.insert_at_start(4)
ll.insert_at_start(3)
ll.insert_at_start(2)
ll.insert_at_start(1)
ll.insert_at_last(6)
ll.insert_at_last(7)
ll.insert_at_last(8)
ll.insert_at_last(9)
ll.insert_at_last(10)
ll.show()
ll.remove(9)
ll.show()
ll.remove(0)
ll.show()
ll.remove(2)
ll.show()
print(f"Length: {ll.get_length()}")
