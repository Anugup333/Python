import re

# matching the tables 
# searches for all digits only
matchtab = re.finditer("[0-9]","AaU72#@8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    