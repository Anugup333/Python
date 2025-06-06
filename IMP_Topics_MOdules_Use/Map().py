# Map function

def add_2(x):
    x += 2
    return x

new_list = [1,3,5,7,9]
print("Original List is ",new_list)
new_list = list(map(add_2,new_list))
print("Modeified List is ",new_list)

# also take  input as

l = list(map(int,input("Enter ").split()))
print(l)