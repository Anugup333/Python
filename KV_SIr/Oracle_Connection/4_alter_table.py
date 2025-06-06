# This Program alter(Modifing the table ) from Python Program to database

import oracledb as odb
def alter_modify_table():
    try:
        conobj = odb.connect("system/1234@localhost/xe")
        print("Pytho Program obtained COnnection of oracle ")
        curobj = conobj.cursor()
        print("Type of curobj = ",type(curobj))
        print("Cursor Object created ")
        qry = """alter table employee modify(eno number(4))"""
        curobj.execute(qry)
        print("Alter Table Successfully in oracle DB")
    except odb.DatabaseError as e :
        print("Problem in Data base : ",e)
        

def alter_add_col():
    try:
        conobj = odb.connect("system/1234@localhost/xe")
        curobj = conobj.cursor()
        qry = """alter table employee add(cname varchar2(10))"""
        curobj.execute(qry)
        print("Alter add col in the Table ")
    except odb.DatabaseError as e:
        print("Problem in Database : ",e)

alter_add_col()