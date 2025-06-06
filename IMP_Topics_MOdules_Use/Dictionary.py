# keys in dictionary must be unique and be of any 
# immutable data types (like string , tuples, numbers)

# if you try to add a duplicate key in dic then 
# the last assignment is retained

dis= {"Name":"Jojn","Country":"USA","ID":101}
print(dis)

# dictionary comprehensions

d = {x: x*2+1 for x in range(1,10)}
print(d)
print(d[5])
# delete an element
del d[1]
print(d)