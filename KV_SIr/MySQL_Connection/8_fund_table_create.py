# Create the Table of Fund transfer 
import mysql.connector as Mysql

try:
    conobj = Mysql.connect(host="localhost",port ="3306",user="root", password = "Ramgup9393@",database="bank")
    curobj = conobj.cursor() 
    qry = f"Create table deposit(acno int primary key, cname varchar(15) not null, bal float not null)"
    curobj.execute(qry)
    print("Table is Created Successfully ")
except Mysql.DatabaseError as e:
    print("Problem in Database ",e)
    