class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # ---------------- Insert Element (Push) -------------------------
    def enqueue(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    # ---------------- Remove Element (Pop) -------------------------
    def dequeue(self):
        if self.head is None:
            raise Exception("Queue is Empty")
        val = self.head.data
        self.head = self.head.next
        return val

    # ---------------- Returns the First Element -------------------------
    def peek(self):
        if self.head is None:
            raise Exception("Queue is Empty")
        return self.head.data

    # ---------------- Returns the Length of Queue -------------------------
    def get_length(self):
        if self.head is None:
            raise Exception("Queue is Empty")
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    # ---------------- Prints the Queue -------------------------
    def display(self):
        if self.head is None:
            raise Exception("Queue is Empty")
        ptr = self.head
        while ptr:
            print(f"|{ptr.data}|--", end="")
            ptr = ptr.next
        print("Null")


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.dequeue())
print(q.get_length())
q.display()
