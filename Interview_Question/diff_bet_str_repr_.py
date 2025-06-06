import datetime

today = datetime.datetime.now()


''' for str() '''

'''
print(today,type(today))
s = str(today)
print(s,type(s))

# by using the we can't convert back its original type
# this is used for given the user friendly data
 
c = eval(s)
print(c,type(c))

'''


''' for repr() '''
print(today,type(today))
s = repr(today)
print(s,type(s))

# by using the we can convert back its original type
# This is used in dubugging and development 
 
c = eval(s)
print(c,type(c))

