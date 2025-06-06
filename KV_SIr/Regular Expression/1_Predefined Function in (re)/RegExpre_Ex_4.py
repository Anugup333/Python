import re

gd = input("Enter a line of text : ")
sp = input("Enter which word u want to search : ")
matchinfo = re.search(sp,gd)
print(type(matchinfo))
if (matchinfo != None):
    print("{} Found in Given Data and search is Successful ".format(sp))
else:
    print("{} does not Found in Given Data and search is Successful ".format(sp))