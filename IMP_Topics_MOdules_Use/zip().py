tup = (1,2,3,4)
lis = [1,2,3,4,5,6]
print(list((zip(tup,lis))))
print(list(zip(tup,lis)))
print([zip(tup,lis)])


for i,j in zip(tup,lis):
    print(type(i))
    print(type(j))
    print(f"{i} and {j}")