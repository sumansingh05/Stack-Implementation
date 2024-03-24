class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item)==0
    
    def push(self,data):
        self.item.append(data)

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
             raise IndexError("Stack is Empty")
        
    def peek(self):
         if not self.is_empty():
            return self.item[-1]
         else:
             raise IndexError("Stack is Empty")

    def size(self):
        return len(self.items)
    

s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top element is:",s1.peek())
print("Removed element is:",s1.pop())
print("Top element is:",s1.peek())

        

       
