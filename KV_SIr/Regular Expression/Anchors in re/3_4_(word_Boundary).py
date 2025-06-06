import re

# \b(word Boundary) 
# ==> Matches a word boundary, which is the position 
#     between a word (alphanumeric character) and a non-word character.

print(re.search(r'\bHello\b',"HelloWorld"))
print(re.search(r'\bHello\b',"Hello World"))


# \B( Non word Boundary ) 
# ==> Matches a position that is not a word boundary


print(re.search(r'\BHello\B',"WorldHello"))
print(re.search(r'\BHello\B',"HelloWorld"))
print(re.search(r'\BHello\B',"World aHellom anuj"))