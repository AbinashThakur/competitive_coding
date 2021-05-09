class stack:
    def __init__(self):
        self.item = []
        self.min_item = -1
    
    def push(self, item):
        if self.min_item == -1:
            self.min_item = item
        elif self.min_item > item:
            val = item*2-self.min_item
            self.min_item = item
            item = val
        else:
            pass
        self.item.append(item)
    
    def pop(self):
        if self.item:
            if self.item[-1]<self.min_item:
                self.min_item = self.min_item*2 - self.item[-1]
            else:
                pass
            return self.item.pop()
        else:
            print("underflow from pop")
            return
    
    def is_empty(self):
        return self.item == []
    
    def get_stack(self):
        if self.item:
            return self.item
        else:
            print("underflow from pop")
            return
    
    def get_min(self):
        return self.min_item

s = stack()
s.push(10)
s.push(30)
s.push(20)
s.push(50)
s.push(5)

print(s.get_stack())
print(s.get_min())
s.pop()
print(s.get_stack())
print(s.get_min())