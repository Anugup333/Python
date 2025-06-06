import re

# matching the tables 
# searches for all lower case letters only
matchtab = re.finditer("[a-z]","AaU72#@8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    
