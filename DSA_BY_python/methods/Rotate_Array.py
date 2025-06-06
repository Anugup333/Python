def rotate(arr,n):
    i = 0
    j = n-2
    while i <= j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
    i = 0
    j = n-1
    while i <= j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
    return arr 
arr = {1,2,3,4,5,6}
print(arr)
n = len(arr)
print(rotate(list(arr),n))