#  Implement Stack By Extending List
class Stack(list):
    def is_empty(self):
        return len(self) == 0
    
    def push(self,data):
        self.append(data)
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")
    
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
    
    def size(self):
        return len(self)
    
    def insert(self,index,data):
        raise AttributeError("No Attribute 'insert' in Stack")

if __name__ == "__main__":
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    s1.push(30)
    s1.pop()
    print(f"Top value = {s1.peek()}")