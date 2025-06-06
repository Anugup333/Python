a = [4,3,2,1]
m = list(map(str,a))
print(*m)
print(m)

b = ["aman","rohit","manoj"]
c = list(zip(a,b))
print(*c)
print(c)

for i,(age,name) in enumerate(c):
    print(i,age,name)

# unzipped 
u = zip(*c)
print(*u)

