# Find missing number in an array(Using summation and XOR operaton )

def get_missing_summation(a):
    n = len(a)+1
    sum1 = 0
    total = n*(n+1)//2
    sum1 = sum(a)
    print(total-sum1)

def get_missing_xor(a):
    n= len(a)
    total_xor = 0
    xor_a = a[0]
    for i in range(1,n):
        xor_a = xor_a^a[i]
    for i in range(1,n+2):
        total_xor = total_xor^i
    
    print(total_xor^xor_a)

a= [1,2,3,4,5,7]  
get_missing_summation(a)
get_missing_xor(a)  