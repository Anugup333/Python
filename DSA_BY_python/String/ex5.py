# Find out pairs with given sum value of an array

def pairs(arr,sum1):
    arr.sort()
    first = 0
    last = len(arr)-1
    while(first<=last):
        if(arr[first]+ arr[last] < sum1):
            first +=1
        elif(arr[first]+arr[last] > sum1):
            last -=1
        else:
            print("Values of pairs are : ", arr[first],"&",arr[last])
            first +=1
            last -=1

arr = [5,7,4,3,9,8,19,21]
sum1 = 17
pairs(arr,sum1)