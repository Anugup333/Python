
# WAP which will search Name and Marks of the Students in the given data

import re
gd ="Rohit got 56 marks ,Rohan got 88 marks ,Ganesh got 99 marks ,Anuj got 66 marks ,Senapati got 68 marks, Rossom got 78 marks"

namelist = re.findall("[A-Z][a-z]+",gd)
markslist = re.findall("\d{2}",gd)

# print(namelist)
# print(markslist)

print('='*50)
print("Student Names with its Marks ")
print('='*50) 
for name,marks in zip(namelist,markslist):
    print("Name : {} ---> Marks : {}".format(name,marks))
print('='*50)