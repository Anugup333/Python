import re

# matching the tables 
# searches for all except  digits or  [^0-9]

matchtab = re.finditer("\D","Aa  U72 #@ 8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    