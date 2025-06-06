import re

# matching the tables 
# Searches for all except Upper Case Letters 
matchtab = re.finditer("[^A-Z]","AaU72#@8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    