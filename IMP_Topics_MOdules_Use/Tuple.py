tup = (1,6,0,3,2,5,9,8,7)

print(sorted(tup))
print(type(sorted(tup)))
print(tuple(sorted(tup)))

# can be use as 
tup2 = (1,2)
(a,b) = tup2
print(f"{a} and {b}")


# can not be used append in tuple
newTup = ()
for i in tup:
    if i>5:
        newTup += (i,)

print(newTup)


# assign a single value by this

ct1 = (2)
ct2 = (2,)
print(type(ct1))
print(type(ct2))

# we cannot change the value of the tuple 

ansh = (1,2,3,4,[7,0,39,88,23])

# you can change the value of tuple inside a mutable object 

ansh[4][1] = 8
print(ansh)