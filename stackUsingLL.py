class Node:
    def __init__(self,data):
        self.item = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        #self.tail = None

    def is_empty(self):
        return self.head is None

    #push a new node in stack
    def push(self,data):
       newNode = Node(data) 
       newNode.next = self.head
       self.head = newNode