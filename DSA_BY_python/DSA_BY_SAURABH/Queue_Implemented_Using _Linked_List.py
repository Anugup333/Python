class Node:
    def __init__(self,data=None,next= None) -> None:
        self.item = data
        self.next = next
    
class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.item_count = 0
    
    def is_empty(self):
        return self.front == None
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.item_count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -= 1
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("No data in the Queue")
        return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("No data in the Queue")
        return self.rear.item
    
    def size(self):
        return self.item_count

if __name__ == "__main__":
    q = Queue()
    try:
        print(q.get_front())
    except IndexError as e:
        print(e)  # same print for this e.args[0]
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    try:
        q.dequeue()
        print(q.get_front())
        print(q.get_rear())
    except IndexError as e:
        print(e)
    print(f"{q.size()} number of elements of the queue ")
    
    
            