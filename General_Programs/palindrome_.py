def check_num_palindrome(num):
    temp = num
    div = 0
    while temp>0:
        div = div*10 + temp % 10
        temp = temp//10

    if div == num:
        print(f"{num} Number is Palindrome")
    else:
        print(f"{num} is not Palindrome") 

def check_array_palindrome(arr):
    no = len(arr)
    for i in range(no):
        if arr[i] != arr[no-i-1]:
            print("Array is not palindrome")
            return
    
    print("Array is Palindrome")

# arr = list(map(int,input("Enter the array: ").split()))
str1 = input('Enter the String: ')
check_array_palindrome(str1)