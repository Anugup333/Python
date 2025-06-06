import re

# matching the tables 
# searches for zero or more k's

matchtab = re.finditer("k*","akaakkaakkkaka")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    