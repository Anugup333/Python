# This Program create a table from Python Program to database

import oracledb as odb
try:
    conobj = odb.connect("system/1234@localhost/xe")
    print("Pytho Program obtained COnnection of oracle ")
    curobj = conobj.cursor()
    print("Type of curobj = ",type(curobj))
    print("Cursor Object created ")
    qry = """create table employee(eno number(3) primary key, 
    name varchar2(10) not null , sal number(5,2) not null)"""
    curobj.execute(qry)
    print("Table created Successfully in oracle DB")
except odb.DatabaseError as e :
    print("Problem in Data base : ",e)