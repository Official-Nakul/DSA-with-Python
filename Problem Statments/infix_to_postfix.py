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
            print("Stack is empty")
            return
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if self.head is None:
            # print("Stack is empty")
            return
        return self.head.data

    def get_length(self):
        if self.head is None:
            # print("Stack is empty")
            return 0
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count


def convert(exp):
    priority = {"+": 1, "-": 1, "*": 2, "/": 2}
    s = Stack()
    postfix_exp = ""

    def priority_check(op1, op2):
        return priority[op1] >= priority[op2]

    for i in exp:
        if i not in "+-*/()":
            postfix_exp = postfix_exp + i
        elif i == "(":
            s.push(i)
        elif i == ")":
            while s.get_length() and s.peek() != "(":
                postfix_exp = postfix_exp + s.pop()
            while s.get_length() and s.peek() == "(":
                s.pop()
        else:
            while s.get_length() and s.peek() != "(" and priority_check(s.peek(), i):
                postfix_exp = postfix_exp + s.pop()
            s.push(i)
    while s.get_length():
        postfix_exp = postfix_exp + s.pop()
    return postfix_exp


infix = input("Enter Infix expression: ")
print(f"Postfix Expression: {convert(infix)}")
