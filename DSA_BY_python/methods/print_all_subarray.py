def printAllSubarray(arr,start,end):
    if end == len(arr):
        return 
    elif start > end:
        printAllSubarray(arr,0,end+1)
    else:
        print(arr[start:end+1])
        printAllSubarray(arr,start+1,end)
        
        
def printAllSubarrayIteration(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])

arr = [1,2,3]
printAllSubarrayIteration(arr)