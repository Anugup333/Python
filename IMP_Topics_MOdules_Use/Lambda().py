mul = lambda num1,num2:num1*num2
print(mul(12,12))

# lambda with filter
list_ = [35,12,69,55,75,14,73]
odd_list = list(filter(lambda num: num % 2 != 0 , list_))
print(odd_list)

# lambda with list comprehension

squares = [lambda num =num :num**2 for num in range(1,11)]
for square in squares:
    print(square(),end=" ")

# Lambda with if else
minimum = lambda x,y:x if x<y else y
print("\n",minimum(34,12))