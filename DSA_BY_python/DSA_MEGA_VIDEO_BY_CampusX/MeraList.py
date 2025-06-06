import ctypes

class MeraList:
    def __init__(self) -> None:
        self.size = 1
        self.n = 0
        # Create a C array with the size = self.size
        self.A = self.__make_array(self.size)
    
    def __len__(self):
        return self.n
    
    def __str__(self):
        # [1,2,3]
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        
        return f"[{result[:-1]}]"
        
    def __getitem__(self,index):
        # Indexing 
        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of Bound'
    
    def __delitem__(self,index):
        # delete
        if 0 <= index < self.n:
            
            for i in range(index,self.n-1):
                self.A[i] = self.A[i+1]
            
            self.n -= 1
    
    def append(self,item):
        if self.n == self.size:
            # resize
            self.__resize(self.size*2)
                
        # append
        self.A[self.n] = item
        self.n += 1
    
    def pop(self):
        if self.n == 0:
            return "Empty list"
        print(self.A[self.n-1])
        self.n = self.n - 1
    
    def clear(self):
        self.n = 0
        self.size = 1
    
    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - not in list'
    
    def insert(self,index,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        
        for i in range(self.n,index,-1):
            self.A[i] = self.A[i-1]
        self.A[index] = item
        self.n += 1
    
    def remove(self,item):
        pos = self.find(item)
        
        if type(pos) == int:
            # delete
            self.__delitem__(pos)
        else:
            return pos
                
            
    
    def __resize(self,new_capicity):
        # Create a new Array with new capicity
        new_A = self.__make_array(new_capicity)
        self.size = new_capicity
        
        # Copy the content of A to new_A
        for i in range(self.n):
            new_A[i] = self.A[i]
        
        # reassign A 
        self.A = new_A
        
    
    def __make_array(self,capacity):
        # Create a C type array(static, referencial) with size capacity
        return (capacity*ctypes.py_object)()
    

l = MeraList()
l.append(1)
l.append('anuj')
l.append(2)
l.append(True)
print(len(l))
print(l)
l.pop()
print(l)
print(l[2])
l.insert(2,'gupta')
l.insert(0,0)
print(l)
print(l.size)
del l[4]
print(l)
del l[0]
print(l)
print(len(l))
l.remove('gupta')
print(l)
print()
print(l)