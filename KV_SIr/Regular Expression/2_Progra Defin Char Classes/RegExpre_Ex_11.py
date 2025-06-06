import re

# matching the tables 
# Searches for all Upper Case and Lower case alphabets only
matchtab = re.finditer("[A-Za-z]","AaU72#@8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    