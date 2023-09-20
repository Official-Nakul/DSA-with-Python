class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # ------------------- Insert at the beginning --------------------------------
    def insert_at_start(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    # ------------------- Insert at the beginning --------------------------------
    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None and self.tail is None:
            self.insert_at_start(data)
            return

        node.prev = self.tail
        if self.tail is not None:
            self.tail.next = node
        self.tail = node

    # ------------------- Remove element at given index --------------------------------
    def remove(self, inx):
        if inx < 0 or inx > self.get_length():
            raise Exception("Invalid index")
        if inx == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        elif inx == self.get_length():
            self.tail = self.tail.prev
            self.tail.next = None
            return
        ptr = self.head
        count = 0
        while ptr:
            if count == inx - 1:
                ptr.next = ptr.next.next
                ptr.next.prev = ptr.next.prev.prev
                return
            count += 1
            ptr = ptr.next

    # ------------------- Insert element at given index --------------------------------
    def insert_at_inx(self, inx, data):
        if inx < 0 or inx > self.get_length():
            raise Exception("Invalid index")
        if inx == 0:
            self.insert_at_start(data)
            return
        elif inx == self.get_length():
            self.insert_at_end(data)
            return
        ptr = self.head
        count = 0
        node = Node(data)
        while ptr:
            if count == inx - 1:
                node.next = ptr.next
                ptr.next = node
                node.prev = ptr
                ptr.next.next.prev = node

                return
            count += 1
            ptr = ptr.next

    # ------------------- Printing List in reverse order using Prev pointer ---------------
    def show_prev(self):
        if self.head is None:
            print("List is Empty")
            return
        ptr = self.tail
        lstr = ""
        while ptr:
            lstr += "<--" + str(ptr.data)
            ptr = ptr.prev
        lstr = "Null" + lstr
        print(f"Printing list using Prev Pointer: {lstr}")

    # ------------------- Printing List in Actual order using Next pointer -----------------------
    def show_next(self):
        if self.head is None:
            print("List is Empty")
            return
        ptr = self.head
        lstr = ""
        while ptr:
            lstr += str(ptr.data) + "-->"
            ptr = ptr.next
        lstr = lstr + "Null"
        print(f"Printing list using Next Pointer: {lstr}")

    # ------------------- Returning Length of list -----------------------
    def get_length(self):
        if self.head and self.tail is None:
            return 0
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count


ll = LinkedList()
ll.insert_at_start(5)
ll.insert_at_start(4)
ll.insert_at_start(3)
ll.insert_at_start(2)
ll.insert_at_start(1)

ll.insert_at_end(6)
ll.insert_at_end(7)
ll.insert_at_end(8)
ll.insert_at_end(9)
ll.insert_at_end(10)

ll.insert_at_inx(5, 50)
# ll.remove(10)
print(f"Length: {ll.get_length()}")
ll.show_next()
ll.show_prev()
