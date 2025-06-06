import re

# matching the tables 
# searching except from a, b and c 
matchtab = re.finditer("[^abc]","AaU72#@8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    
