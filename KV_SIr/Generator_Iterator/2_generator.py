# Same as range data type in python

def krange(start=1,stop=1,step=1):
    if start>stop:
        stop =start
        start = 0
    
    while(start<=stop):
        yield start 
        start +=step
        

for val in krange(10):
    print(val)