def takeinput():
    num = int(input("Enter the number of list Element: "))
    input_list = list()
    print("="*50)
    for i in range(1,num+1):
        temp = input(f"Enter the {i} Element in list: ")
        input_list.append(temp)
    return input_list

def solve():
    count = 0
    for num in lst:
        if len(num) >=2 and num[0] == num[-1]:
            count +=1
    print(f"List Elements is {lst}")
    print(f"No of Count is {count}")

lst = takeinput()
print("="*50)
solve()
