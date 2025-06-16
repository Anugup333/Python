class SpaceError(Exception): pass
class ZeroLengthError(Exception): pass
class InvalidNameError(Exception): pass

def validate(name):
    if(name.isspace()):
        raise SpaceError
    else:
        words = name.split()
        if len(words) == 0:
            raise ZeroLengthError
        else:
            temp = True
            for word in words:
                if(not word.isalpha()):
                    temp = False
                    break
            if temp:
                return name
            else:
                raise InvalidNameError
        
try:
    name = input("enter the name of Student: ")
    valid_name = validate(name)
except SpaceError:
    print("\tDon't enter the Space in the Name ")
except ZeroDivisionError:
    print("\tMust Enter the Name ")
except InvalidNameError:
    print("\tInvalid Name")
else:
    print("\tValid Name : ",valid_name)