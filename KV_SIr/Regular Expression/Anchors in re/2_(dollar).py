import re

# $(dollar) ==>  End of a String



print(re.findall(r'\d$',"Hello World1"))
print(re.findall(r'\s$',"World "))
print(re.findall(r'\s$',"World"))

