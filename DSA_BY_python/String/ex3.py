# Conversion of two list into the dictionary in python

def list_to_dict():  # sourcery skip: inline-immediately-returned-variable
    keys = [1,2,3]
    values  = ["One", "Two","Three"]
    result = dict(zip(keys,values))
    return result

def dict_to_tuple():
    x = list_to_dict()
    for i in x.items():
        print(i)

dict_to_tuple()