def takeinput():
    num = int(input("Enter the number of list Element: "))
    input_list = list()
    print("="*50)
    for i in range(1,num+1):
        temp = tuple(input(f"Enter the {i} Two Element in Tuple of list: ").split())
        input_list.append(temp)
    return input_list

def sort_last_tuple():
    temp = sorted(lst,key=lambda x:x[-1]) # Best
    print("="*50)
    print(f"Sorted List of tuples Based on second Element {temp}")

lst = takeinput()
sort_last_tuple()