import re

# matching the tables 
# searches for all except word characters( Special Symbols)  or [^A-Za-z0-9]

matchtab = re.finditer("\W","Aa  U72 #@ 8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    