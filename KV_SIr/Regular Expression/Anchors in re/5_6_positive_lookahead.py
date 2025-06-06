import re

#  (?=...) (Positive Lookahead)
# ==> Matches a position where what follows matches 
#      the pattern inside the lookahead

print(re.search(r'cat(?= fish)', 'The cat fish is fast'))
print(re.search(r'The(?= fish)', 'The cat fish is fast'))


# (?!...) (Negative Lookahead)
# ==> Matches a position where what follows does not 
#       match the pattern inside the lookahead.


print(re.search(r'cat(?! fish)', 'The cat is fast'))
print(re.search(r'The(?! cat)', 'The cat fish is fast'))
