import re

# matching the tables 
# searches for all digits or  [0-9]

matchtab = re.finditer("\d","Aa  U72 #@ 8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    