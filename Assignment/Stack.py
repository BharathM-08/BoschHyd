class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if(self.isEmpty()):
            print("Stack is Empty")
        else:
            return self.stack.pop()
    
    def peek(self):
        if(self.isEmpty()):
            print("Stack is Empty")
        else:
            return (self.stack[-1])

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

cl = Stack()
cl.push('A')
cl.push('B')
cl.push('C')
print("The elements in Stack :")
cl.display()
print("Size before popping: ",cl.size())
print("Peeking :",cl.peek())
print("Popping :",cl.pop())
print("Size after  popping: ",cl.size())
print("Peeking :",cl.peek())
print("The elements in Stack after popping :")
cl.display()
