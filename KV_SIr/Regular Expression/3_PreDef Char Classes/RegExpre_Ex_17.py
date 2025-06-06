import re

# matching the tables 
# searches for all space Characters 

matchtab = re.finditer("\s","Aa  U72 #@ 8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    