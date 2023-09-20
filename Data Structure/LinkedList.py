class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # ---------------------------- Insert at Start --------------------------

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    # ---------------------------- Insert at Last --------------------------
    def insert_at_last(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            """
            it is same as 
            node=Node(data,self.head)
            self.head=node
            """
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(data)

    # ---------------------------- Insert at Position --------------------------
    def insert_at(self, inx, data):
        if inx < 0 or inx > self.get_length():
            raise Exception("Invalid Index")
        if self.head is None:
            self.insert_at_start(data)
            return
        ptr = self.head
        count = 0
        while ptr:
            if count == inx - 1:
                ptr.next = Node(data, ptr.next)
                # ptr = ptr.next.next
            ptr = ptr.next
            count += 1

    # ---------------------------- Search by Index --------------------------

    def search_by_inx(self, inx):
        if self.head is None:
            raise Exception("List is Empty")
        elif inx < 0 or inx > self.get_length():
            raise Exception("Enter Valid Index")
        count = 0
        ptr = self.head
        while ptr:
            if count == inx:
                print(f"Value at Index {inx} is {ptr.data}")
                return
            count += 1
            ptr = ptr.next

    # ---------------------------- Search by Value --------------------------
    def search_by_Value(self, val):
        if self.head is None:
            raise Exception("List is Empty")
        ptr = self.head
        inx = 0
        while ptr:
            if val == ptr.data:
                print(f"Value {ptr.data} is at Index {inx}")
                return
            ptr = ptr.next
            inx += 1
        print(f"{val} is not in the List")

    # ---------------------------- delete by Index --------------------------
    def delete_by_inx(self, inx):
        if self.head is None:
            raise Exception("List is Empty")
        elif inx < 0 or inx > self.get_length():
            raise Exception("Enter Valid Index")
        count = 0
        ptr = self.head
        while ptr:
            if count == inx - 1:
                ptr.next = ptr.next.next
                print(f"Value at Index {inx} is Removed")
                return
            count += 1
            ptr = ptr.next

    # ---------------------------- delete by Value --------------------------
    def delete_by_val(self, val):
        if self.head is None:
            raise Exception("List is Empty")
        ptr = self.head

        if self.head.data == val:
            self.head = self.head.next
            print(f"{val} is Removed")
            return

        while ptr.next:
            if ptr.next.data == str(val):
                ptr.next = ptr.next.next
                print(f"{val} is Removed")
                return
            ptr = ptr.next
        print(f"{val} is not in the List")

    # ---------------------------- Get length of List --------------------------
    def get_length(self):
        if self.head is None:
            raise Exception("List is Empty")
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    # ---------------------------- Print the List --------------------------
    def show(self):
        if self.head is None:
            raise Exception("List is Empty")
        ptr = self.head
        lstr = ""
        while ptr:
            lstr = lstr + str(ptr.data) + "-->"
            ptr = ptr.next
        lstr += "Null"
        print(lstr)


ll = LinkedList()

user_opt = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

print("1.Insert At the Start\n\
2.Insert At the End\n\
3.Insert At the Index\n\
4.Search Element by Index\n\
5.Search Element by Value\n\
6.Delete Element by Index\n\
7.Delete Element by Value\n\
8.Print LinkedList\n\
9.Print the Length of Linked List\n\
10.Exit")
print("-------------------------------")

# ---------------------------- Loop to ask user choice multiple times --------------------------
while True:
    user_input = int(input("Enter your Choice: "))
    if user_input in user_opt:
        if user_input == 1:
            val = input("Enter Value: ")
            ll.insert_at_start(val)
            print("***********************")
        elif user_input == 2:
            val = input("Enter Value: ")
            ll.insert_at_last(val)
            print("***********************")
        elif user_input == 3:
            inx = int(input("Enter index: "))
            val = input("Enter Value: ")
            ll.insert_at(inx, val)
            print("***********************")
        elif user_input == 4:
            inx = int(input("Enter Index: "))
            ll.search_by_inx(inx)
            print("***********************")
        elif user_input == 5:
            val = input("Enter Value: ")
            ll.search_by_Value(val)
            print("***********************")
        elif user_input == 6:
            inx = int(input("Enter Index: "))
            ll.delete_by_inx(inx)
            print("***********************")
        elif user_input == 7:
            inx = input("Enter Value: ")
            ll.delete_by_val(inx)
            print("***********************")
        elif user_input == 8:
            ll.show()
            print("***********************")
        elif user_input == 9:
            print(f"Length of List is {ll.get_length()}")
            print("***********************")
        elif user_input == 10:
            break
    else:
        print("Enter Valid Number")
