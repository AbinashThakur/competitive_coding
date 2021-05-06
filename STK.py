class stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def is_empty(self):
        return self.items == []
    
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("Underflow")
            return
    
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Underflow")
            return
        
    def get_stack(self):
        return self.items

s = stack()
print(s.is_empty())
s.push(1)
s.push(5)
s.push(4)
s.push(6)
print(s.get_stack())
print(s.peek())
s.pop()
s.pop()
print(s.get_stack())
print(s.peek())
print(s.is_empty())