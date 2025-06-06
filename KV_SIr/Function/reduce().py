# reduce() present in functools.reduce
# Which is ised to perform 
# existing  sum(), max(), min(), function internally use reduce()

from functools import reduce

lst = [int(i) for i in input("Enter list: ").split()]

sum_list = lambda lst: reduce(lambda x,y: x+y,lst)
max_list = lambda lst: reduce(lambda x,y: x if x>y else y,lst)
min_list = lambda lst: reduce(lambda x,y: x if x<y else y,lst)


print("Sum of list: ",sum_list(lst))
print("Max Value of list: ",max_list(lst))
print("Min Value of list: ",min_list(lst))
