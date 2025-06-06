# this program is used to insert data 

import oracledb as odb
try:
    conobj = odb.connect("system/1234@localhost/xe")
    curobj = conobj.cursor()
    # design the query        
    qry = """insert into employee values(2,'Anuj',200.0,'TCS')"""
    curobj.execute(qry)
    conobj.commit()
    print("first record is recorded ")
except odb.DatabaseError as e:
    print("Problem in the data",e)
