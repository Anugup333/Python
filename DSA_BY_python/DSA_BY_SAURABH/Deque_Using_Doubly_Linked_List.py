class Node:
    def __init__(self,data=None,prev=None,next=None) -> None:
        self.prev = prev
        self.item = data
        self.next = next
    
class Deque:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.item_count = 0
    
    def is_empty(self):
        return self.front == None
    
    def insert_front(self,data):
        new_node = Node(data,None,self.front)
        if self.is_empty():
            self.rear = new_node
        else:
            self.front.prev = new_node
        
        self.front = new_node
        self.item_count += 1
    
    def insert_rear(self,data):
        new_node = Node(data,self.rear)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node 
        self.item_count += 1
    
    def delete_front(self):
        if not self.is_empty():
            self.front = self.front.next
            self.front.prev = None
        elif self.front == self.rear:
            self.front = None    
            self.rear = None    
        else:
            raise IndexError("Deque is Empty")
        self.item_count -= 1
    
    def delete_rear(self):
        if not self.is_empty():
            self.rear = self.rear.prev
            self.rear.next = None
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            raise IndexError("Deque is Empty")
        self.item_count -= 1
    
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("deque is Empty")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("deque is Empty")
    
    def size(self):
        return self.item_count

if __name__ == "__main__":
    d = Deque()
    d.insert_front(10)
    d.insert_front(20)
    d.insert_rear(30)
    d.insert_rear(40)
    print(d.get_front())
    print(d.get_rear())
    print(f"{d.size()} elements in Deque")
   