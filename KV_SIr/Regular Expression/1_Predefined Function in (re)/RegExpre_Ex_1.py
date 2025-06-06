import re
gd = "Python is an Oops Lang. Python is also Functional Programming Lang."

sp = "Python"
mtab = re.finditer(sp,gd)
print(type(mtab))
noc = 0

for omt in mtab:
    noc += 1
    print("Start Index : {} End Index : {} Value : {}".format(omt.start(),omt.end(),omt.group()))
else:
    print("="*50)
    print("Number of Occurances of {} : {} ".format(sp,noc))
    