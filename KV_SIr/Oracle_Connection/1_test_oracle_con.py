import oracledb


try:
    # connect("username/password @ IP Address/Service Id")
    conobj = oracledb.connect("system/1234@localhost/xe")
    print(conobj) 
    print("Type of con var = ",type(conobj))
    print("Python Program got Connection from Oracle DB")
except oracledb.DatabaseError as db:
    print("Problem in Connection : ",db)
finally:
    conobj.close()
    print("Python Closes the Connection from Oracle db")