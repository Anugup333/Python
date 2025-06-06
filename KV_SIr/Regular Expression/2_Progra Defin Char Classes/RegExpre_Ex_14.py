import re

# matching the tables 
# Searches for all except digits 
matchtab = re.finditer("[^0-9]","AaU72#@8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    