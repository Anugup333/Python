class Queue:
    def __init__(self) -> None:
        self.items = list()
        # self.front = None
        # self.rear = None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,data):
        self.items.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue Underflow")
    
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue Underflow")
    
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue Underflow")
    
    def size(self):
        return len(self.items)

# if __name__ == "__main__":
#     q = Queue()
#     try:
#         print(q.get_front())
#     except IndexError as e:
#         print(e)  # same print for this e.args[0]
#     q.enqueue(10)
#     q.enqueue(20)
#     q.enqueue(30)
#     q.enqueue(40)
#     try:
#         q.dequeue()
#         print(q.get_front())
#         print(q.get_rear())
#     except IndexError as e:
#         print(e)
#     print(f"{q.size()} number of elements of the queue ")