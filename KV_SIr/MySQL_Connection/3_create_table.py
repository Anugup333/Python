# Create the Table 
import mysql.connector as Mysql

try:
    conobj = Mysql.connect(host="localhost",port ="3306",user="root", password = "Ramgup9393@",database="kvr_db")
    curobj = conobj.cursor() 
    qry = f"Create table employee (eno int primary key, ename varchar(10) not null, esal real not null )"
    curobj.execute(qry)
    print("Table is Created Successfully ")
except Mysql.DatabaseError as e:
    print("Problem in Database ",e)
    