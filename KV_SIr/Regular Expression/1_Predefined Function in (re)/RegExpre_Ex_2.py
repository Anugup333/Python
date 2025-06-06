import re
gd = "Python is an Oops Lang. Python is also Functional Programming Lang."

sp = "Python"
mtab = re.findall(sp,gd)
print(type(mtab))
print(mtab)
print("="*50)
print("Number of Occurances of {} : {} ".format(sp,len(mtab)))
