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
        lstr = "Null" + lstr + "-->Null"
        print(f"Printing list using prev Pointer: {lstr}")

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
        lstr = "Null<--" + lstr + "Null"
        print(f"Printing list using next Pointer: {lstr}")


ll = LinkedList()
ll.insert_at_start(10)
ll.insert_at_start(20)
ll.insert_at_start(30)
ll.insert_at_start(40)
ll.insert_at_start(50)
ll.show_prev()
ll.show_next()
