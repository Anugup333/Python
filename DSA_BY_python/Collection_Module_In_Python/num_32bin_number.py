# a = f"{10:032b}"
# print(a)
# n = 10
# b = "{:032b}".format(n)
# print(b)

# print(int("111",2))

n = 29
d = 2
strd = f"{d:016b}"
print(strd)        
last = strd[16-d:] + strd[:16-d]
print(last)
print([n<<d,int(last,2)])