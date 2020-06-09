"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage =[]
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         return self.storage.insert(0, value)

#     def dequeue(self):
#         return self.storage.pop() if self.storage else None

# class Node: 
#     # Function to initialise the node object 
#     def __init__(self, data): 
#         self.data = data # Assign data 
#         self.next = None # Initialize next as null 
# class LinkedList: 
  
#     # Function to initialize head 
#     def __init__(self): 
#         self.head = None
#         self.tail = None
  
# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def __len__(self): 
#         temp = self.head # Initialise temp 
#         count = 0 # Initialise count 
  
#         # Loop while end of linked list is not reached 
#         while (temp): 
#             count += 1
#             temp = temp.next
#         return count 
#     def enqueue(self, data):
#         if self.tail is None:
#             self.head = Node(data)
#             self.tail = self.head
#         else:
#             self.tail.next = Node(data)
#             self.tail = self.tail.next
 
#     def dequeue(self):
#         if self.head is None:
#             return None
#         else:
#             to_return = self.head.data
#             self.head = self.head.next
#             return to_return
import sys
sys.path.append('./linkedlist.py')
from linkedlist import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    def __len__(self):
        return self.size
    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        if self.size is not 0:
            self.size -= 1
            return self.storage.remove_head()