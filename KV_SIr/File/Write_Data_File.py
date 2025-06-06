# Program Reading the Data from KBD and write that data to the file 

import sys
with open("name.txt","w") as fp:
    print("Enter the Lines of Text and press 'quit' to stop ")
    while(True):
        indata = input()
        if(indata == "quit"):
            sys.exit()
        else:
            fp.write(indata+"\n")