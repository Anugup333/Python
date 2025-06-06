def partition(arr,low,high):
    # pivot is pointed to the High
    pivot = arr[high]
    # create  to point less low 
    i = low - 1
    for j in range(low,high):
        if arr[j] <= pivot:
            # if pivot is equal to the j 
            i += 1
            # swap element at i with j 
            arr[i], arr[j] = arr[j], arr[i]
    # swap the pivot element with the greater element specified by i
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i + 1
    
        
def quick_sort(arr , low ,high):
    if low < high :
        # Find pivot element such that 
        # element smaller than the pivot is left 
        # element greater than the pivot are at the right 
        pi = partition(arr,low,high)
        # recursive call the left to the pivot - 1
        quick_sort(arr,low,pi-1)
        # recursive call the pivot + 1 to the right 
        quick_sort(arr,pi + 1, high)
    return arr

if __name__ == "__main__":
    arr = [12,5,0,161,1,28,4,9]
    print("array is \n",arr)
    arr = quick_sort(arr,0,len(arr)-1)
    print("Sorted array is \n",arr)
        