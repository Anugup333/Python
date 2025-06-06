print('''------ Generator -------''') 

def my_generator(start,end):
    for i in range(start,end+1):
        yield i*i

# gen = list(my_generator(3,9))
# print(gen)

gen = my_generator(3,9)
print("By using next function ",next(gen))
print("This the object reference ",gen)
for num in gen:
    print(num)



print('''----- Iterator -----''')

# By default of the iterator 
iter_list = iter([1,2,33,32,22,2])
print("By using next function ",next(iter_list))

print("By loop")
for i in iter_list:
    print(i)

print('''------- defining iterator class by user --------''')

class Myiterator:
    def __init__(self,start,end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        temp = self.current
        self.current += 1
        return temp

for i in Myiterator(1,5):
    print(i)
