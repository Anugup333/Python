import array

arr = array.array('i',[1,2,3,4,5])
# i represent integer 

print(arr)
print(arr[0])
arr.append(6)
arr.remove(3)
for element in arr:
    print(element)
