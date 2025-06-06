s = set()
s2 = {}
print(type(s))
print(type(s2))


# set is an unordered type data structure and it is mutable
s3 = {1,5,4,8,6}
print(s3)

# inside set we give only only immuable objects 
s4 = {1,2,"Anuj",(6,27,83)}

print(s4)
try:
    s5 = {1,2,"Anuj",[6,27,83]}
    print(s5)
except:
    print("we can not give mutable object inside set")

# Frozenset is an immutable version of the built-in set it is similar to the set but its content can not be changed once a frozen set is created

fset = frozenset([1,2,3,4,5])
print(fset)     

# it can be use as 
dis= {"Name":"Jojn","Country":"USA","ID":101}

dkey = frozenset(dis)
print(dkey)

# Program 
odds = set([2*i+1 for i in range(1,10)])
print(odds)
primes = set()
for i in range(2,20):
    j = 2
    flag = 0
    while j<i/2:
        if i%j == 0:
            flag = 1
        j += 1
    if flag == 0:
        primes.add(i)
print(primes)
print("UNION : ",odds.union(primes))
print("INTERSECTION : ",odds.intersection(primes))
print("SYMMETRIC DIFFERENCE : ",odds.symmetric_difference(primes))
print("DIFFERENCE : ",odds.difference(primes))