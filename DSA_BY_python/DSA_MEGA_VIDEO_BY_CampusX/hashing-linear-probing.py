class Ditionary:
    def __init__(self,size) -> None:
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def put(self,key,value):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                new_hash_value = self.rehash(hash_value)
                
                while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key:
                    new_hash_value = self.rehash(hash_value)
                
                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                else:
                    self.data[new_hash_value] = value
    
    def get(self,key):
        start_position = abs(self.hash_function(key))
        current_position = start_position
        
        while self.slots[current_position] != None:
            if self.slots[current_position] == key:
                return self.data[current_position]
            
            current_position = abs(self.rehash(current_position))

            if current_position == start_position:
                return 'Not Found'
        return 'None wala - Not Found'    
    
    def __str__(self) -> str:
        
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(self.slots[i],':',self.data[i],end=" ")
        
        return ""
    
    def __getitem__(self,key):
        return self.get(key)
                
    def __setitem__(self,key,value):
        self.put(key,value)       
    
    def rehash(self,old_hash):
        return (old_hash + 1) % self.size
                
    def hash_function(self,key):
        return abs(hash(key)) % self.size


d = Ditionary(5)
d['python'] = 45
d['java'] = 55
d['php'] = 100
d['php'] = 1000
d['python'] = 134
print(d.slots)
print(d.data)
print(d['python'])
print(d['java'])
print(d['php'])
print(d['c'])
print(d)