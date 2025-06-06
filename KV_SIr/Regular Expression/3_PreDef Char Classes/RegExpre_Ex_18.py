import re

# matching the tables 
# searches for all except space Characters 

matchtab = re.finditer("\S","Aa  U72 #@ 8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    