class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = None
    
    def append(self,val):
        Newnode = Node(val)
        if self.head == None:
            Newnode.next = None
            self.head = Newnode
            return 
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Newnode

    def printLinkedlist(self):
        if self.head == None:
            print("List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next


lt = linklist()
lt.append(1)
lt.append(2)
lt.append(3)
lt.append(4)
lt.append(5)
lt.printLinkedlist()
            