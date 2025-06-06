def takeinput():
    num = int(input("Enter the number of list Element: "))
    input_list = list()
    print("="*50)
    for i in range(1,num+1):
        temp = input(f"Enter the {i} Element in list: ")
        input_list.append(temp)
    return input_list

def remove_duplicates():
    lst = takeinput()
    print("="*50)
    print(f"The List of the Elements {lst}")
    for i in lst:
        if i in lst:
            lst.remove(i)
    print("="*50)
    print(f"Distinct List of Elements {lst}")

remove_duplicates()        