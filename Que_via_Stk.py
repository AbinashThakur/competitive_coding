class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    
    def enqueue(self, x):
        while len(self.stack1)!=0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()
            
        
        self.stack1.append(x)
        
        while len(self.stack2)!=0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
        return self.stack1

    def dequeue(self):
        if len(self.stack1)!=0:
            x = self.stack1[-1]
            self.stack1.pop()
            return self.stack1
        else:
            print("The Stack is Empty")

q = Queue()
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))

print(q.dequeue())
print(q.dequeue())