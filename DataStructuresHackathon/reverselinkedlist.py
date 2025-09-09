class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist2:
    def __init__(self):
        self.head = None

    def append(self,val):
        Newnode = Node(val)
        if(self.head == None):
            Newnode.next = None
            self.head = Newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Newnode

    def reversell(self):
        prev = None
        currentnode = self.head
        while currentnode: 
            nextnode = currentnode.next
            currentnode.next = prev
            prev = currentnode
            currentnode = nextnode

        self.head = prev

    def printLinkedlist(self):
        if self.head == None:
            print("List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,end = " ")
                temp =temp.next


lt = Linkedlist2()
lt.append(1)
lt.append(2)
lt.append(3)
print("Before Reversal :")
lt.printLinkedlist()
revhead = lt.reversell()
print("\nAfter Reversal :")
lt.printLinkedlist()



