# This Program get the Connection and create the cursor Object 

import oracledb as odb
conobj = odb.connect("system/1234@localhost/xe")
print("Pytho Program obtained COnnection of oracle ")
curobj = conobj.cursor()
print("Type of curobj = ",type(curobj))
print("Cursor Object created ")
