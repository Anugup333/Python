import re

# matching the tables 
# search either a,b and c from data 
matchtab = re.finditer("[abc]","AaU72#@8sbbioapnPoc")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    
