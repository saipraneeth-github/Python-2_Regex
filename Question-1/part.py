class stack:
        def __init__(self, capacity):
                self.top = -1
                self.capacity = capacity
                
                self.array = []
              
            
        def isEmpty(self):
                return True if self.top == -1 else False
              

        def peek(self):
                return self.array[-1]
              

        def pop(self):
                if not self.isEmpty():
                        self.top -= 1
                        return self.array.pop()
                else:
                        return "$"
              
          
        def push(self, op):
                self.top += 1
                self.array.append(op) 

