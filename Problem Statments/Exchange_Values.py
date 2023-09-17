class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        if self.head is None:
            print("Stack is Empty")
            return
        val = self.head.data
        self.head = self.head.next
        return val

    def get_length(self):
        if self.head is None:
            print("Stack is Empty")
            return 0
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    def show(self):
        if self.head is None:
            print("Stack is Empty")
            return
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def exchange(self, inx1, inx2):
        global s, s1, s2
        ptr1 = s.head
        ptr2 = s.head
        count1 = count2 = 0

        while count1 != inx1:
            count1 += 1
            ptr1 = ptr1.next
        s1.push(ptr1.data)

        while count2 != inx2:
            count2 += 1
            ptr2 = ptr2.next
        s2.push(ptr2.data)

        s.change(count1, s2.pop())
        s.change(count2, s1.pop())

    def change(self, inx, val):
        global s, s1, s2

        if self.head is None:
            raise Exception("Stack is Empty")
        elif inx < 0 or inx > self.get_length():
            raise Exception("Invalid index")
        ptr = self.head
        count = 0
        while ptr:
            if count == inx:
                ptr.data = val
                break
            count += 1
            ptr = ptr.next


s = Stack()
s1 = Stack()
s2 = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print("----Before Exchange-----")
s.show()
print("----After Exchange-----")
s.exchange(0, 4)
s.show()
