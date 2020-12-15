# Create classes
# Note: -1 on start and top denotes empty queue
class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1 
    
    # Print Queue
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    # isFull (if pointers next to eachother or opposite ends)
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    # isEmpty
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    # enqueue (if top points to last element, go back to start. Also, set top to 0 if first element)
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"
    
    # dequeue (if only one element, set top and start back to -1, else increment to next)
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]

    # delete
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1





# Trials
customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.delete()
print(customQueue)