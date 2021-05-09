class setofstack:
    def __init__(self,capacity):
        self.stacks = []
        if capacity<1:
            print("Can't have stacks of that height")
        else:
            self.capacity = capacity
            
    def push(self, item):
        if self.stacks == []:
            self.stacks.append([item])
        else:
            if len(self.stacks[-1])>=self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)
    
    def pop(self):
        if self.stacks == []:
            print("Can't pop an empty stack")
        else:
            popped_item = self.stacks[-1][-1]
            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                del self.stacks[-1][-1]
            return popped_item

s = setofstack(4)
for i in range (1,15):
	s.push(i)
print(s.stacks)

s.pop()
print(s.stacks)

s.pop()
print(s.stacks)