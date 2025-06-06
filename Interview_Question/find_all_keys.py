dict1 = {1:1,2:4,3:9,4:16,5:25}

# first Type

# all_keys = list(dict1.keys())
# print(all_keys) 

# Second Type

# all_keys = list(dict1)
# print(all_keys) 

# third Type

# all_keys = [*dict1.keys()]
# print(all_keys) 

# fourth Type

# all_keys = [*dict1]
# print(all_keys) 

#  fifth Type

# all_keys = dict1.keys()
# print([k for k in all_keys]) 


# Sixth Type

# *all_keys, = dict1.keys()
# print(all_keys) 

# Seventh Type

*all_keys, = dict1
print(all_keys) 
print(dict1)

del dict1[2]
print(dict1)

