
# WAP for searching Names and marks of the Students information by reading text document from file 
  

import re

try:
    with open("student.data") as fp:
        filedata = fp.read()
        namelist = re.findall("[A-Z][a-z]+",filedata)
        markslist = re.findall("\d{2}",filedata)
        print('='*50)
        print("Student Names with its Marks ")
        print('='*50) 
        for name,marks in zip(namelist,markslist):
            print("Name : {} ---> Marks : {}".format(name,marks))
        print('='*50)
        
except FileNotFoundError:
    print("File not Found in the directory")