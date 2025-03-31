from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
       
    
    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.popleft()
           
            return removed
        else:
            print("Queue is empty.")
            return None
        
    def peek(self):
        if not self.is_empty():
            print(f"Front of queue: {self.queue[0]}")
            return self.queue[0]
        else:
            print("Queue is empty.")
            return None
            
    def is_empty(self):
        return len(self.queue) == 0    
    
    def size(self):
        print(f"Queue size: {len(self.queue)}")
        return len(self.queue)
    
    def display(self):
        print("Queue: ", list(self.queue))    
        
cities = Queue()
cities.enqueue("Harar")
cities.enqueue("Mekelle")
cities.enqueue("Hawassa")

cities.dequeue()
cities.display()