"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         return self.storage.append(value)

#     def pop(self):
#         return self.storage.pop() if self.storage else None

# Node class 
# class Node: 
#     # Function to initialise the node object 
#     def __init__(self, data): 
#         self.data = data # Assign data 
#         self.next = None # Initialize next as null 
  
  
# Linked List class contains a Node object 
# class LinkedList: 
  
#     # Function to initialize head 
#     def __init__(self): 
#         self.head = None

# class Stack:
#     def __init__(self):
#         self.head = None
 
#     def push(self, data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             new_node = Node(data)
#             new_node.next = self.head
#             self.head = new_node
 
#     def pop(self):
#         if self.head is None:
#             return None
#         else:
#             popped = self.head.data
#             self.head = self.head.next
#             return popped
#         # This function counts number of nodes in Linked List 
#     # iteratively, given 'node' as starting node. 
#     def __len__(self): 
#         temp = self.head # Initialise temp 
#         count = 0 # Initialise count 
  
#         # Loop while end of linked list is not reached 
#         while (temp): 
#             count += 1
#             temp = temp.next
#         return count 

import sys
sys.path.append('./linkedlist.py')
from linkedlist import LinkedList

#stack implementaiton w/ linked list
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    def __len__(self):
        return self.size
    def push (self, value):
        self.size +=1
        self.storage.add_to_tail(value)
    def pop(self):
        if self.size is not 0:
            self.size -= 1
            return self.storage.remove_tail()
        else:
            return None