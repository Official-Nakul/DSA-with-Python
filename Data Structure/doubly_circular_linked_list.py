class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        node = Node(data)

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            self.head.prev = self.tail
            self.tail.next = self.head
            return
        self.tail.next = node
        self.head.prev = node
        node.next = self.head
        node.prev = self.tail
        self.head = node

    def get_length(self):
        ptr = self.head
        count = 0
        while ptr.next != self.head:
            count += 1
            ptr = ptr.next
        return count + 1

    def show_next(self):
        ptr = self.head
        lstr=""
        for i in range(self.get_length()):
            lstr += str(ptr.data) + "-->"
            ptr = ptr.next
        lstr = lstr + "Head"
        print(lstr)

    def show_prev(self):
        ptr = self.tail
        lstr = ""
        for i in range(self.get_length()):
            lstr += "<--" + str(ptr.data)
            ptr = ptr.prev
        lstr = "Tail" + lstr
        print(lstr)


ll = DoublyCircularLinkedList()

ll.insert_at_start(3)
ll.insert_at_start(2)
ll.insert_at_start(1)
ll.show_next()
ll.show_prev()
print(f"Length: {ll.get_length()}")
