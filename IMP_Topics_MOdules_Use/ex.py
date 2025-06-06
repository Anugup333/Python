# def findCommon(ar1, ar2, ar3, n1, n2, n3):

#     # Initialize starting indexes for ar1[], ar2[] and ar3[]
#     i, j, k = 0, 0, 0
#     ans = set()
#     # Iterate through three arrays while all arrays have elements
#     while (i < n1 and j < n2 and k < n3):

#         # If x = y and y = z, print any of them and move ahead
#         # in all arrays
#         if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
#             ans.add(ar1[i])
#             i += 1
#             j += 1
#             k += 1

#         # x < y
#         elif ar1[i] < ar2[j]:
#             i += 1 

#         # y < z
#         elif ar2[j] < ar3[k]:
#             j += 1

#         # We reach here when x > y and z < y, i.e., z is smallest
#         else:
#             k += 1
#     return ans


# # Driver program to check above function
# ar1 = [1, 5, 10, 20, 40, 80,80]
# ar2 = [6, 7, 20, 80,80, 100]
# ar3 = [3, 4, 15, 20, 30, 70, 80,80, 120]
# n1 = len(ar1)
# n2 = len(ar2)
# n3 = len(ar3)
# print("Common elements are ",findCommon(ar1, ar2, ar3, n1, n2, n3))

# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *=i
#     return fact

# def factorialAgain(n, p):
#     first = fact(3*n)
#     print(first)
#     sec = 6**n
#     print(sec)
#     last = first // sec
#     print(last)
#     print(last%p)
#     return last %p

# print(factorialAgain(4,7))

# nums = ["3","6","7","10"]
# k = 4
# print(nums)
# nums = sorted(nums)
# print(nums)
# # print(str(l))

s = [3,4,10,8,4,1,2]
s.
print(s)