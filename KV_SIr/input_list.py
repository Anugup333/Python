n = int(input("Enter the n number : "))
if(n<0):
    print(f"{n} is Invalid input ")
else:
    print("="*50)
    lst =[]
    for i in range(1,n+1):
        temp = int(input(f"Enter {i} integer Value : "))
        lst.append(temp)
    else:
        lst.sort()
        print("="*50)
        print(f"List is Elements in Ascending Order : {lst}")
        print(f"List is Elements in Descending Order : {lst[::-1]}")