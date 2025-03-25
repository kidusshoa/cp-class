class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            removed = self.items.pop()
            print(f"Popped: {removed}")
            return removed
        else:
            print("Stack is empty.")
            return None
    def peek(self):
        if not self.is_empty():
            print(f"Top element: {self.items[-1]}")
            return self.items[-1]
        else:
            print("Stack is empty.")
            return None
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        print(f"Stack size: {len(self.items)}")
        return len(self.items)
    
    def display(self):
        print("Current stack", self.items)
        
names = Stack()
names.push("Sinaf")
names.push("Dave")
names.push("Hayat")
names.push("Miftah")

names.push("Dave")

names.display()
