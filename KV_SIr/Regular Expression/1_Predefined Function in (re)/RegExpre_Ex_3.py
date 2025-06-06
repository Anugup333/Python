import re
gd = "Python is an Oops Lang. Python is also Functional Programming Lang."

sp = "Python"
matchinfo = re.search(sp,gd)
print(type(matchinfo))

if (matchinfo != None):
    print("First Match of {} start Index : {} and End Index : {}".format(sp,matchinfo.start(),matchinfo.end()))
else:
    print("Not Found ")