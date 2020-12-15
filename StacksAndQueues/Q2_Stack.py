
#   Create Stack with min method (retains min value in stack)

# Create node class
class Node():
    def __init__(self, value=None, next = None):
        self.value = value
        self.next = next
    
    # Makes printable
    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string

 # Stack class
class Stack():
    def __init__(self):
        self.top = None
        self.minNode = None

    # min return
    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value
    
    # push (each time update min node)
    def push(self, item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value = self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value = item, next=self.minNode)
        self.top = Node(value=item, next=self.top)
    
    # pop (keep track min node to next)
    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item

# Trial 

customStack = Stack()
customStack.push(5)
print(customStack.min())
customStack.push(6)
print(customStack.min())
customStack.push(3)
print(customStack.min())
customStack.pop()
print(customStack.min())

