def fabonacci(n):
    if(n<2):
        return 1
    else:
        return fabonacci(n-1) + fabonacci(n-2)

n = int(input("Enter the Numbers of terms : "))
for i in range(n):
    print(f"\t{fabonacci(i)}",end="")