import re

# matching the tables 
# searches for all the occurance of letters of the given data

matchtab = re.finditer(".","akaakkaakkkaka")

print(type(matchtab))

for one in matchtab:
    print("Start : {} End : {}  Value : {}".format(one.start(),one.end(),one.group()))
    