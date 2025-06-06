fruits = ["Apple","banana","Apricot"]

map_obj = map(lambda s: s[0]=="A",fruits)
filter_obj = filter(lambda s: s[0]=="A", fruits)

from functools import reduce
lst = [2,4,5,6]
print(reduce(lambda x,y: x+y,lst))



print(list(map_obj))
print(list(filter_obj))