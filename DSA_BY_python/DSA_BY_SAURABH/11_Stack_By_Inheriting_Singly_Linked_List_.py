from Singly_Linked_list_ import *

class Stack(SLL):
    
    def __init__(self):
        super().__init__()
        self.item_count = 0
    
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.item_count +=1
    
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -= 1
        else:
            raise SyntaxError("Stack UnderFlow")
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:  
            raise SyntaxError("Stack Underflow")        
    
    def size(self):
        return self.item_count
    
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top element is ",s.peek())
    s.pop()
    print("Top element is ",s.peek())
    