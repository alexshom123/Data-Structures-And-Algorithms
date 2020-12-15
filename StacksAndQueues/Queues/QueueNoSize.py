# Create classes
class Queue:
    def __init__(self):
        self.items = []

    # Makes printable
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    # enqueue
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"
    
    # dequeue
    def dequeue(self):
        if self.isEmpty():
            return "The is not any element in the Queue"
        else:
            return self.items.pop(0)
    
    # peek
    def peek(self):
        if self.isEmpty():
            return "The is not any element in the Queue"
        else:
            return self.items[0]
    # delete
    def delete(self):
        self.items = None



# Trials
customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())
customQueue.delete()
