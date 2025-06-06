import random
n = random.randint(2,8)   
print("Randint: ",n)

n1 = random.randrange(2,4)   # 2 wala element nahi lete h 
print("Randrange: ",n1)

i = [10,20,30,40]
lc = random.choice(i)
print("Random Choice: ",lc)

r = random.random()    # between 0 and 1 float value
print("Random: ",r)

l = [10,20,30,40]
random.shuffle(l)    # list Shuffle 
print("Shuffle: ",l)

u = random.uniform(3,9)   # between 3 and 9 float value
print("Uniform: ",u)