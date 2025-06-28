'''
Sort given Array which is already Sorted based on absolute values of elements
Last Updated : 17 Jan, 2024
Given an array arr[] of size N, sorted based on the absolute value of its elements. The task is to sort this array based on the actual values of the elements.

Examples: 

Input:  arr[] = 11, -7, 5, 10, 18
Output: {5, -7, 10, -11, 18}-
Explanation: When the array is sorted the negative values will come at the beginning of the array.



Input:  arr[] = {1, -2, -3, 4, -5}
Output: -5, -3, -2, 1, 4

'''

arr1 = [-5, -3, -2, 1, 4]

def swapf(i,j,arr):
    if(abs(arr[j]) <= abs(arr[i])):
        arr[i],arr[j] = arr[j],arr[i]
        


def sort_absolute(arr):
    i =0 
    j = len(arr)-1
    while j != i:
        if abs(arr[i]) > abs(arr[i+1]):
            swapf(i,j,arr)
            j-=1
        else:
            arr[i],arr[i+1] = arr[i+1],arr[i] 
            swapf(i,j,arr)
            j-=1

    return arr 

print(sort_absolute(arr1))
            