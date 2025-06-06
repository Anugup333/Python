import re

# matching the tables 
# searches for all alpha-numeric()

matchtab = re.finditer("[A-Za-z0-9]","AaU72#@8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    