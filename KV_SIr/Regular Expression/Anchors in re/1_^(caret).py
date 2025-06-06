import re

# ^(Caret) ==> is used for Matches the position 
#                 at the beginning of the string.

print(re.findall(r'^Hello',"Hello World"))
print(re.findall(r'^Hello',"World"))

