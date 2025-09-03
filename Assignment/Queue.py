class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if(self.isEmpty()):
            return "Queue is Empty"
        return self.queue.pop(0)

    def peek(self):
        if(self.isEmpty()):
            return "Queue is Empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print(self.queue)

qu = Queue()
qu.enqueue('A')
qu.enqueue('B')
qu.enqueue('C')
print("Elements in Queue :")
qu.display()
print("Size before dequeue :",qu.size())
print("Dequeue :",qu.dequeue())
print("Size after  dequeue :",qu.size())
print("Peeking :",qu.peek())
print("Elements in Queue after dequeuing :")
qu.display()

