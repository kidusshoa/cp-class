class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def display(self):
        current = self.head
        if current is None:
            print("List is empty.")
            return
        
        print("Linked List:", end = "   ")
        while current:
            print(current.data, end= " --> ")
            current = current.next
        print("None")
        
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            print(f"{key} not found in the list.")
            return
        
        prev.next = current.next
        
#usage example
courses = LinkedList()
courses.insert_at_end("Python")
courses.insert_at_end("Java")
courses.insert_at_beginning("C++")
courses.insert_at_beginning("C#")
courses.display()

courses.delete("Java")
courses.display()
