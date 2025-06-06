# def checkRedundancy(Str):
     
#     # create a stack of characters 
#     st = [] 
 
#     # Iterate through the given expression 
#     for ch in Str: 
 
#         # if current character is close 
#         # parenthesis ')' 
#         if (ch == ')'): 
#             top = st[-1] 
#             st.pop() 
 
#             # If immediate pop have open parenthesis 
#             # '(' duplicate brackets found 
#             flag = True
 
#             while (top != '('): 
 
#                 # Check for operators in expression 
#                 if (top == '+' or top == '-' or
#                     top == '*' or top == '/'): 
#                     flag = False
 
#                 # Fetch top element of stack 
#                 top = st[-1] 
#                 st.pop()
 
#             # If operators not found 
#             if (flag == True):
#                 return True
 
#         else:
#             st.append(ch) # append open parenthesis '(', 
#                           # operators and operands to stack
#     return False

# def findRedundantBrackets(s:str):
# 	# Write your code here.
# 	# Return boolean True or False.
# 	# stack
#     ans = checkRedundancy(s)
#     if ans == True:
#         return "Yes"
#     else:
#         return "No"

# print(findRedundantBrackets("(a+b)"))
# a = 5
# b = a
# b = b+1
# print(a,b)


# def pairSum(arr, n, target):
#     # Write your code here.
#     start = 0
#     end = n-1
#     count = 0
#     while start < end:
#         curr_sum = arr[start] + arr[end]
#         if curr_sum < target:
#             start +=1
#         elif curr_sum > target :
#             end -=1
#         else:
#             count +=1
#             start +=1
#             end -=1
#     if count == 0:
#         return -1
#     else:
#         return count


# arr= [1,2,3,4,5,6]
# print(pairSum(arr,len(arr),7))
# from collections import Counter
# arr = [1,2,3,4,1]
# d  = dict(Counter(arr))
# print(d)
# for i in d:
#     if d[i] > 1:
#         print(i)
#         break

def linear(data,n,item):
    for i in range(n):
        if data[i] == item:
            return i+1
        
    


print(linear([1,2,3,4,5,6],6,1))


