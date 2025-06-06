import re

#  (?<=...) (Positive Lookbehind)

# ==> Matches a position where what precedes the current position 
#       matches the pattern inside the lookbehind.

print(re.search(r'(?<=The )cat', 'The cat fish is fast'))
print(re.search(r'(?<= fish )cat', 'The cat fish is fast'))


# (?<!...) (Negative Lookbehind)
# ==> Matches a position where what precedes the current position 
#      does not match the pattern inside the lookbehind.


# Matches 'cat' only if it's **not** preceded by 'the'
print(re.search(r'(?<!The )cat', 'The cat is fast'))  # No Match
print(re.search(r'(?<!anuj )cat', 'A cat is fast'))  # Match