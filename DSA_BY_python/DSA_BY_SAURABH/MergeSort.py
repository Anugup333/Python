def merge_sort(list,left,right):
    if left<right:
        mid = (left + right)//2 
        merge_sort(list,left,mid)
        merge_sort(list,mid+1,right)
        merge(list,left,mid,right)

def merge(list,left,mid,right):
    leftlist = list[left:mid+1]
    rightlist = list[mid+1:right+1]
    i,j,k = 0,0,left
    while i<len(leftlist) and j<len(rightlist):
        if leftlist[i] <= rightlist[j]:
            list[k] = leftlist[i]
            i+=1
        else:
            list[k] = rightlist[j]
            j+=1
        k+=1
    while i<len(leftlist):
        list[k] = leftlist[i]
        i+=1
        k+=1
        
    while i<len(rightlist):
        list[k] = rightlist[i]
        j+=1
        k+=1

arr = [12,23,1,11,122,2,5,6,7,8]
merge_sort(arr,0,len(arr)-1)
print(arr)
        
    