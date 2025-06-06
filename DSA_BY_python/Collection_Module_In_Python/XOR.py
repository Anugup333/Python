# # 1. Finding the missing Number in an array (1 to N)
# def missing(arr):
#     n = len(arr) +1
#     xor_all = 0
#     for i in range(1,n+1):
#         xor_all ^=i
#     for num in arr:
#         xor_all ^=num
#     return xor_all

# # print(missing([1,2,3,5]))
# print(8)

s = 1<<3
print(s)