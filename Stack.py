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
        print(f"{val} removed")

    # ------------ Prints the value at the top of the Stack----------------
    def peek(self):
        return self.head.data

    # ------------ Prints the Stack----------------
    def change(self, inx, val):
        if self.head is None:
            raise Exception("Stack is Empty")
        elif inx < 0 or inx > self.get_length():
            raise Exception("Invalid index")
        ptr = self.head
        count = 0
        while ptr:
            if count == inx:
                ptr.data = val
                print(f"Value at Index {inx} is updated with {val}")
                break
            count += 1
            ptr = ptr.next

    # ------------ Update Stack with Value ----------------
    def replace(self, new_val, old_val):
        if self.head is None:
            raise Exception("Stack is Empty")
        ptr = self.head
        while ptr:
            if ptr.data == old_val:
                ptr.data = new_val
                print(f"{old_val} is updated with {new_val}")
                return
            ptr = ptr.next
        print(f"{old_val} is not in the Stack")

    # ------------ Prints the Stack----------------
    def show(self):
        ptr = self.head
        while ptr:
            print("|   |")
            print(f"| {ptr.data} |")
            print("|___|")
            ptr = ptr.next

    # ------------ Returns the length of Stack"----------------
    def get_length(self):
        if self.head is None:
            raise Exception("Stack is Empty")
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count


s = Stack()

user_opt = (1, 2, 3, 4, 5, 6, 7, 8)

print("1.Push\n\
2.Pop\n\
3.Peek\n\
4.Print the Stack\n\
5.Get Length of the Stack\n\
6.Update value with index\n\
7.Replace value\n\
8.Exit")
print("-------------------------------")

# ---------------------------- Loop to ask user choice multiple times --------------------------
while True:
    user_input = int(input("Enter your Choice: "))
    if user_input in user_opt:
        if user_input == 1:
            val = input("Enter Value: ")
            s.push(val)
            print("***********************")
        elif user_input == 2:
            s.pop()
            print("***********************")
        elif user_input == 3:
            print(f"Value at the Top {s.peek()}")
            print("***********************")
        elif user_input == 4:
            s.show()
            print("***********************")
        elif user_input == 5:
            print(f"Length of Stack is {s.get_length()}")
            print("***********************")
        elif user_input == 6:
            inx = int(input("Enter Index: "))
            val = input("Enter value: ")
            s.change(inx, val)
            print("***********************")
        elif user_input == 7:
            old_val = input("Enter Old Value: ")
            new_val = input("Enter New Value: ")
            s.replace(new_val, old_val)
            print("***********************")
        elif user_input == 8:
            break
    else:
        print("Enter Valid Number")
