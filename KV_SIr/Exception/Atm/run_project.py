from atm_demo import sbi
import getpass 
import sys
def runatm():
    count = 0
    while True:
        pin = getpass.getpass(prompt="Enter your Pin: ")
        if pin == "6765":
            sbi()
        else:
            print("\t Pin is Invalid , try again ")
            count+=1
            if count == 3:
                print("Your Card Blocked ")
                sys.exit()