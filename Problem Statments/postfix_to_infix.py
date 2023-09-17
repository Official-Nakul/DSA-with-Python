class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    # ------------ Add the element "Push"----------------
    def push(self, data):
        self.head = Node(data, self.head)

    # ------------ Remove the element "Pop"----------------
    def pop(self):
        val = self.head.data
        self.head = self.head.next
        return val

    # ------------ Prints the value at the top of the Stack----------------
    def peek(self):
        if self.head is None:
            return
        return self.head.data

    # ------------ Prints the Stack----------------
    def show(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    # ------------ Returns the length of Stack"----------------
    def get_length(self):
        if self.head is None:
            return 0
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count


s = Stack()
postfix = input("Enter PostFix Expression: ")
for i in postfix:
    if i in "+-*/":
        val1 = s.pop()
        val2 = s.pop()
        val = val2 + i + val1
        s.push(val)
    else:
        s.push(i)

print(f"Infix Expression: {s.peek()}")
