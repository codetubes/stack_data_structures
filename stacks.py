class Container():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Stack():
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[len(self.items) -1]
    
    def size(self):
        return len(self.items)

myStack = Stack()
myStack.push(Container(name="cont1",weight=1500))
myStack.push(Container(name = "cont2", weight = 7000))
myStack.push(Container(name = "cont3", weight = 4500))
myStack.push(Container(name = "cont4", weight = 12000))

#print(myStack.top().name, myStack.top().weight)

currentContainer = myStack.pop()
print(currentContainer.name, currentContainer.weight)
print(myStack.size())

currentContainer = myStack.pop()
print(currentContainer.name, currentContainer.weight)
print(myStack.size())





    
