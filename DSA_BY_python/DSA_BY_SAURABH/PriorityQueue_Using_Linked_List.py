class Node:
    def __init__(self,item = None,priority = None,next = None) -> None:
        self.item = item
        self.priority = priority
        self.next = next
    
class PriorityQueue:
    def __init__(self) -> None:
        self.start = None
        self.item_count = 0
    
    def push(self,data,priority):
        new_node = Node(data,priority)
        if not self.start or priority < self.start.priority:
            new_node.next = self.start
            self.start = new_node
        else:
            temp = self.start 
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.item_count += 1
    
    def is_empty(self):
        return self.start == None
    
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data    
        else:
            raise IndexError("PriorityQueue is Empty")
    
    def size(self):
        return self.item_count

if __name__ == "__main__":
    p = PriorityQueue()
    p.push("Amit",4)
    p.push("Arjun",7)
    p.push("Ashima",2)
    p.push("Agrah",5)
    p.push("Anant",8)
    p.push("Ambika",1)
    print(f"{p.size()} elements")
    
    while not p.is_empty():
        print(p.pop())
    
    print(f"{p.size()} elements")