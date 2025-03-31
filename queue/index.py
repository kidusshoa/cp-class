class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty.")
            return None
    
    def peek(self):
        if not self.is_empty():
            print(f"Front of Queue: {self.items[0]}")
            return self.items[0]
        else:
            print("Queue is empty.")
            return None
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        print(f"Queue size: {len(self.items)}")
        return len(self.items)
    
    def display(self):
        print("Queue:", self.items)
        
Students = Queue()
Students.enqueue("Tinsae")
Students.enqueue("Yabets")
Students.enqueue("Terefe")

# Students.display()
# Students.peek()
# Students.dequeue()
# Students.display()
Students.size()