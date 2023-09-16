class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

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

    def get_length(self):
        if self.head is None:
            raise Exception("List is Empty")
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count

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
4.Element At Index\n\
5.Search Element by Index\n\
6.Search Element by Value\n\
7.Delete Element by Index\n\
8.Delete Element by Value\n\
9.Print LinkedList\n\
10.Print the Length of Linked List\n\
11.Exit")
print("-------------------------------")
while True:
    user_input = int(input("Enter your Choice: "))
    if user_input in user_opt:
        if user_input == 1:
            val = input("Enter Value: ")
            ll.insert_at_start(val)
        elif user_input == 2:
            val = input("Enter Value: ")
            ll.insert_at_last(val)
        elif user_input == 3:
            inx = int(input("Enter index: "))
            val = input("Enter Value: ")
            ll.insert_at(inx, val)
        elif user_input == 4:
            val = input("Enter Value: ")
            ll.insert_at_last(val)
        elif user_input == 5:
            inx = int(input("Enter Index: "))
            ll.search_by_inx(inx)
        elif user_input == 6:
            val = input("Enter Value: ")
            ll.insert_at_last(val)
        elif user_input == 7:
            val = input("Enter Value: ")
            ll.insert_at_last(val)
        elif user_input == 8:
            val = input("Enter Value: ")
            ll.insert_at_last(val)
        elif user_input == 9:
            ll.show()
        elif user_input == 10:
            ll.get_length()
        elif user_input == 11:
            break
    else:
        print("Enter Valid Number")
