# This Program is used to create the Custom Iterator

class MyIterator:
    def __init__(self,obj):
        self.obj = obj
        self.limit = len(obj)
        self.start = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.limit:
            result = self.obj[self.start]
            self.start += 1
            return result
        else:
            raise StopIteration

obj = MyIterator("Py")
print(next(obj))
print(next(obj))
print(next(obj))