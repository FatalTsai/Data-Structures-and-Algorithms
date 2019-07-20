# A queue that only has enqueue and dequeue operations
# First-in-First-Out (FIFO) 
#   enqueue - adds an element to the end of the queue
#   dequeue - removes the element at the beginning of the queue


class Queue:
    def __init__(self):
        self.queue = []
       
    def isEmpty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 

        
