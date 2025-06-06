def takeinput():
    num = int(input("Enter the number of list Element: "))
    input_list = list()
    print("="*50)
    for i in range(1,num+1):
        temp = int(input(f"Enter the {i} Element in list: "))
        input_list.append(temp)
    return input_list

# Example 1
def sum_list():
    sum = 0
    for i in lst:
        sum +=i
    print("="*50)
    print(f"List Elements {lst} ")
    print(f"Sum of List Elements {sum} ")
    print("="*50)

def mul_list():
    mul = 1
    for i in lst:
        mul *=i
    print("="*50)
    print(f"List Elements {lst} ")
    print(f"Multiply of List Elements {mul} ")
    print("="*50)

def max_list():
    max = float("-inf")
    for i in lst:
        if i>max:
            max = i
    print("="*50)
    print(f"List Elements {lst} ")
    print(f"Max Element of List Elements {max} ")
    print("="*50)

def min_list():
    min = float("+inf")
    for i in lst:
        if i<min:
            min = i
    print("="*50)
    print(f"List Elements {lst} ")
    print(f"Min Element of List Elements {min} ")
    print("="*50)
    
lst = takeinput()
sum_list()
mul_list()
max_list()
min_list()