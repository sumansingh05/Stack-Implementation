class Node:
    def __init__(self,data):
        self.item = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0
        #self.tail = None

    def is_empty(self):
        return self.head is None

    #push a new node in stack
    def push(self,data):
       newNode = Node(data) 
       newNode.next = self.head
       self.head = newNode
       self.count += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            temp = self.head.item
            self.head = self.head.next
            self.count -= 1
            return temp
        
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.head.item

    def size(self):
        return self.count
    
    def display(self):
        current = self.head
        print("Stack is:",end=" ")
        while(current):
            print(current.item,end=" ")
            current = current.next
    

s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.display()
print()
print("Total element in the stack:",s1.size())
print("Top element in the stack:",s1.peek())
print("Poped element is:",s1.pop())
s1.display()
print()
print("Total element in the stack:",s1.size())
print("Top element in the stack:",s1.peek())
