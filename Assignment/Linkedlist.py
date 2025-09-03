class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def prepend(self,data):
        newnode = Node(data)
        if(self.head == None):
            self.head = newnode
            self.next = None
        else:
            newnode.next = self.head
            self.head = newnode

    def append(self,data):
        if not self.head:
            self.prepend(data)
            return
        newnode = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode

    def delete(self,val):
        temp = self.head
        while temp.next == val:
            temp = temp.next
        temp.next = temp.next.next

        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp = temp.next

ll = linkedlist()
ll.append(10)
ll.prepend(5)
ll.append(30)
ll.delete(10)
ll.display()
    