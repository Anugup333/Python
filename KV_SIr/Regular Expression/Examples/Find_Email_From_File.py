# WAP to retrieve and Validate the Email id of Different Students where student information present in the file

import re
try:
    with open("studentinfo.data") as fp:
        filedata = fp.read()
        emaillist = re.finditer('\S+@\S+',filedata)
        print('='*50)
        print("All Email of Students")
        for obj in emaillist:
            print("Email : ",obj.group())
        print('='*50)
except FileNotFoundError:
    print("File Not found ")