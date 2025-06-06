import copy

orignal_list = [[1,2,3],[4,5,6]]
shallow_copy_list = copy.copy(orignal_list)
deep_copy_list = copy.deepcopy(orignal_list)

# modifying the shallow copy 
shallow_copy_list[0][0] = 99
deep_copy_list[0][0] = 38

print("Original List: ",orignal_list)
print("Shallow Copy List: ",shallow_copy_list)
print("Deep copy List: ",deep_copy_list)
