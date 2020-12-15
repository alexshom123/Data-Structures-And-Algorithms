
# Implement a queue using two stacks.

# Base class for stack
class Stack():
  def __init__(self):
    self.list = []
  
  # len of list
  def __len__(self):
    return len(self.list)
  
  # push
  def push(self, item):
    self.list.append(item)
  
  # pop
  def pop(self):
    if len(self.list) == 0:
      return None
    return self.list.pop()

# QueueviaStack stack from two normal stacks
class QueueviaStack():
  def __init__(self):
    self.inStack = Stack()
    self.outStack = Stack()
  
  # push (to instack)
  def enqueue(self, item):
    self.inStack.push(item)
  
  # dequeue (push in to out then out to in and pop)
  def dequeue(self):
    while len(self.inStack):
      self.outStack.push(self.inStack.pop())
    result = self.outStack.pop()
    while len(self.outStack):
      self.inStack.push(self.outStack.pop())
    return result
  
# Trial 
customQueue = QueueviaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
customQueue.enqueue(4)
print(customQueue.dequeue())