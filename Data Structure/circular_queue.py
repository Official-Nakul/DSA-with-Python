class CircularQueue:
    def __init__(self, size):
        self.num = [None] * size
        self.head = -1
        self.tail = -1
        self.size = size

    def insert(self, data):
        if (self.tail + 1) % self.size == self.head:
            print("Queue is full")
            return
        if self.head == -1 and self.tail == -1:
            self.tail = 0
            self.head = 0
            self.num[self.tail] = data
            return
        self.tail = (self.tail + 1) % self.size
        self.num[self.tail] = data

    def remove(self):
        if self.head == -1:
            print("Queue is Empty")
            return
        val = self.num[self.head]
        if self.tail == self.head:
            self.tail = self.head = -1
            return val
        self.head = (self.head + 1) % self.size
        return val

    def show(self):
        ptr = self.head
        while True:
            if ptr == self.tail:
                break
            print(self.num[ptr])
            ptr = (ptr + 1) % self.size

    def is_empty(self):
        return self.tail == -1 and self.head == -1

    def peek(self):
        return self.num[self.head]


q = CircularQueue(5)
q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
print(f"Removed: {q.remove()}")
print(f"Removed: {q.remove()}")
q.insert(6)
q.insert(7)
print(f"Removed: {q.remove()}")
q.insert(8)
while not q.is_empty():
    print(q.peek())
    q.remove()
