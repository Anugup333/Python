class Node:
    def __init__(self,item = None, next = None) -> None:
        self.item = item
        self.next = next

class CLL:
    def __init__(self,last = None) -> None:
        self.last = last
    
    def is_empty(self):
        return self.last == None
    
    def insert_at_start(self,data):
        new_node = Node(data)
        if not self.is_empty():
            new_node.next = self.last.next
            self.last.next = new_node
        else:
            self.last = new_node
            new_node.next = new_node
    
    def insert_at_last(self,data):
        new_node = Node(data)
        if not self.is_empty():
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node
        else:
            self.last = new_node
            new_node.next = new_node
    
    def search(self,data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            new_node = Node(data,temp.next)
            temp.next = new_node
            if temp == self.last:
                self.last = new_node
    
    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item,end=" ")
                temp = temp.next
            print(temp.item)
    
    def delete_at_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next
    
    def delete_at_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next 
                self.last = temp
    
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item == data:
                    self.last.next = self.last.next.next
                else:
                    temp = self.last.next
                    while temp != self.last:
                        if temp.next.item == data:
                            if temp.next == self.last:
                                temp.next = self.last.next
                                self.last = temp
                                break
                            else:
                                temp.next = temp.next.next
                                break
                        temp = temp.next\
    
    def __iter__(self):
        if self.last == None:
            return None
        else:
            return CLLiterator(self.last.next)
                    

class CLLiterator:
    def __init__(self,start = None) -> None:
        self.current = start
        # preserve the reference of the first node
        self.start = start
        self.count = 0
    
    def __iter__(self):
        return self
    
    def  __next__(self):
        
        if self.current is None:
            raise StopIteration 
        
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
            
        data = self.current.item
        self.current = self.current.next
        
        return data       
        

if __name__ == "__main__":
    # Driver Code 
    mylist = CLL()
    mylist.insert_at_start(20)
    mylist.insert_at_start(10)
    mylist.insert_at_last(30)
    mylist.insert_after(mylist.search(20),25)
    mylist.insert_after(mylist.search(10),15)
    
    for i in mylist:
        print(i,end=" ")
    print()
    
    mylist.delete_at_last()
    
    mylist.delete_at_first()
    
    mylist.delete_item(20)
    
    mylist.print_list()
    
    for i in mylist:
        print(i)
    print()