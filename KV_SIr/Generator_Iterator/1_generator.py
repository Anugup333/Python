# generator 

def kvrrange(start,stop):
    while(start<=stop):
        yield start
        start +=1
        
x = kvrrange(1,5)
print("Type of kvrrange = ",type(kvrrange))
print("Type of x = ",type(x))

# first Access 

# try:
#     print(next(x))
#     print(next(x))
#     print(next(x))
#     print(next(x))
#     print(next(x))
#     print(next(x))
# except StopIteration:
#     print("kvrrange out of range ")


# Second Access
for val in x:
    print(val)