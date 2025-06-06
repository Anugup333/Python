# 1

cubes = [i**3 for i in range(11)]
print(cubes)

# 2 
 
tu = [(x,y) for x in [10,20,30] for y in [20,30,98] if x != y]
print(tu)

# 3

no_dub = [x for x in [1,2,3,1,2,4,5,2,4,2,4,5] if x not in [1,2,3]]
print(no_dub)

# 4 

l = [10,20,30,40,50,60,70,80,90]
enu = [(index,i) for index,i in enumerate(l)]
print(enu)