class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,data):
        self.append(data)

    def pop(self):
        