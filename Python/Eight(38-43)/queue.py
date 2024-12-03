class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} pushed into the queue.")
    
    def dequeue(self):
        if self.is_empty():
            return "The queue is empty"
        else:
            return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return "The queue is empty"
        return self.queue[0]
    
    def size(self):
        return len(self.queue)



queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue()) 
print(queue.peek())
print(queue.size())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
