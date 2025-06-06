def merge(arr1,arr2):
    i =0
    j =0
    ans = []
    while i<len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i +=1
        else:
            ans.append(arr2[j])
            j +=1
    
    while i<len(arr1):
        ans.append(arr1[i])
        i +=1
        
    while j < len(arr2):
        ans.append(arr2[j])
        j +=1
    
    return ans


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left,right)

if __name__ == "__main__":
    arr = [12,5,0,161,1,28,4,9]
    print("array is \n",arr)
    arr = merge_sort(arr)
    print("Sorted array is \n",arr)
