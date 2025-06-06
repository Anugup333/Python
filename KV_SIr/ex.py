# import matplotlib.pyplot as pt
# import numpy as np
# itcrs = ["Python","Java","C","CPP"]
# usage = np.array([60,40,20,20])
# pt.pie(usage,labels=itcrs)
# pt.show()

# print("Enter the old salary of employees by space : ")
# oldsal = [float(val) for val in input().split()]
# hikesal = list(map(lambda val:val*(1.5),oldsal))
# print("="*50)
# print("Old Salary\tNew Salary")
# print("="*50)
# for old,new in zip(oldsal,hikesal):
#     print(f"{old}\t\t{new}")
# print("="*50)



# print("Enter the elements by space : ")
# lst = [int(val) for val in input().split()]
# poslst = list(filter(lambda val: val>0,lst))
# neglst = list(filter(lambda val: val<0,lst))
# possqr = list(map(lambda val: val**2,poslst))
# negsqr = list(map(lambda val: val**2,neglst))
# print("="*50)
# print("Pos Val \t Srquare Val")
# print("="*50)
# for old,new in zip(poslst,possqr):
#     print(f"{old}\t\t{new}")
# print("="*50)
# print("="*50)
# print("Neg Val \t Srquare Val")
# print("="*50)
# for old,new in zip(neglst,negsqr):
#     print(f"{old}\t\t{new}")
# print("="*50)

# import functools
# lst1 = [23,45,78,8,9]
# # lst2 = [8,9,5,47,67,78]
# # lst3 = list(map(lambda i,j:i+j,lst1,lst2))
# # print(lst1)
# # print(lst2)
# # print(lst3)
# sum_list = functools.reduce(lambda x,y:x+y,lst1)
# max_list = functools.reduce(lambda x,y:x if x>y else y,lst1)
# min_list = functools.reduce(lambda x,y:y if x>y else x,lst1)
# print(sum_list)
# print(max_list)
# print(min_list)


# import sys
# sys.path.append("C:/Users/DELL/OneDrive/Desktop/Python/KV_SIr/MenuDrivenApplication")
# from MenuDrivenApplication.aopdemo import menu
# menu()

# import os

# # print(os.listdir())

# for dirpath, dirnames, filenames in os.walk("OS_Module"):
#     print(f"Directory: {dirpath}")
#     print(f"Subfolders: {dirnames}")
#     print(f"Files: {filenames}")


# print(pow(2,3,5))


# shallow cloning
# ------------------------
# import copy
# x = [10,20,[30,40],50]
# y = copy.copy(x)
# y[2][0] = 333
# print('x:',id(x))
# print('y:',id(y))
# print('x:',x)
# print('y:',y)

# Deep cloning
# --------------------
# import copy
# x = [10,20,[30,40],50]
# y = copy.deepcopy(x)
# y[2][0] = 333
# x[2][1] = 999
# print('x:',id(x))
# print('y:',id(y))
# print('x:',x)
# print('y:',y)

from faker import Faker
from datetime import date

fakerobj = Faker()
def generate():
    count = 1
    def display_fake_entry():
        nonlocal count
        rollno = count
        count +=1
        name = fakerobj.name()
        dob = fakerobj.date_between_dates(date_start=date(2001,4,6),date_end=date(2003,4,6)).strftime("%d-%m-%Y")
        marks = fakerobj.random_int(50,100)
        email = fakerobj.email()
        phonenumber = fakerobj.random_int(min=6666666666,max=9999999999)
        address = fakerobj.city()
        return (rollno,name,dob,marks,email,phonenumber,address)
    return display_fake_entry

gen = generate()
ans = [gen() for i in range(200)]

for val in ans:
    print(val)