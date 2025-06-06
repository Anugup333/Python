class Deque:
    def __init__(self) -> None:
        self.items = list()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def insert_front(self,data):
        self.items.insert(0,data)
    
    def insert_rear(self,data):
        self.items.append(data)
    
    def delete_front(self,data):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Deque is Empty")
    
    def delete_rear(self,data):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("Deque is Empty")
    
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Deque is Empty")
    
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Deque is Empty")
    
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    d = Deque()
    d.insert_front(10)
    d.insert_front(20)
    d.insert_rear(30)
    d.insert_rear(40)
    print(d.get_front())
    print(d.get_rear())
