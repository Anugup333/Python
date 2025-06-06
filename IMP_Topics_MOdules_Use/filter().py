# this is same as map fuction but slite difference 

def check(x):
    if (x % 2 == 0 or x % 4 == 0):
        return 1

evens = list(filter(check,range(2,22)))
print(evens)

# that return as list of string

innu = list(filter(int,input("Enter ").split()))
print(innu)