
# WAP Which is Evaluate or validate mobile number  

import re 

while True:

    mno = input("Enter your Mobile Number : ")
    
    if len(mno) == 10:
        varname = re.search("\d{10}",mno)
        if varname != None:
            print("Mobile Number is Valid ")
            break
        else:
            print("\nMobile Number should only Contain digits ")
    else:
        print("\nYour mobile should contain 10 digits in length")
    
    