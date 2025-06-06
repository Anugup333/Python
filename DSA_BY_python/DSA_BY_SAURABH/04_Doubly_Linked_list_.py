"""Soubly Linked List """
class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next
    
class DLL:
    def __init__(self,start = None):
        self.start = start
        
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        new_node = Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev = new_node
            self.start = new_node
        else:
            self.start = new_node
    
    def insert_at_last(self,data):
        new_node = Node(None,data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else:
            self.start = new_node
    
    def search(self,data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next
        else:
            return None
        
    def insert_after(self,temp,data):
        if temp is not None:
            new_node = Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = new_node
            temp.next = new_node
    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
    
    def delete_at_first(self):
        if not self.is_empty():
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
    
    def delete_at_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
    
    def delete_item(self,data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next
                            
    def __iter__(self):
        return DLLiterator(self.start)
    

class DLLiterator:
    def __init__(self,start) -> None:
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data        
    

if __name__ == "__main__":
    # Driver Code 
    mylist = DLL()
    mylist.insert_at_start(20)
    mylist.insert_at_start(10)
    mylist.insert_at_last(30)
    mylist.insert_after(mylist.search(20),25)
    mylist.insert_after(mylist.search(10),15)
    
    mylist.delete_at_last()
    
    mylist.delete_at_first()
    
    mylist.delete_item(20)
    
    mylist.print_list()
    print()
    
    for i in mylist:
        print(i)
    print()





