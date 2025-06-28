""" 
Problem statement : 

You have two numbers number1 and number2, your job is to check the number of borrow operations needed for subtraction of number1 from number2. If the subtraction is not possible
then return the string not possible.

Example :

754
658

Answer :

2
654
666"""


# Solution: 

num_1 = int(input())
num_2 = int(input())

count = 0
if(num_1 < num_2):
    print("not possible")
else:
    flag = 0
    while num_1 != 0 or num_2 != 0:
        temp1 = 0
        temp2 = num_2 % 10
        if flag:
            temp1 = num_1 % 10 - 1 
        else:
            temp1 = num_1 % 10
        
        if temp1 < temp2:
            flag = 1
            count +=1
        else:
            flag = 0
        num_1 = num_1 //10
        num_2 = num_2 //10
    print(count)
        