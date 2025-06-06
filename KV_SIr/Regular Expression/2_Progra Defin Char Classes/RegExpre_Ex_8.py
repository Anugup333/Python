import re

# matching the tables 
# searches for all except lower case letters
matchtab = re.finditer("[^a-z]","AaU72#@8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    
