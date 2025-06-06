# This program create a database in Mysql on the name of 

import mysql.connector as Mysql 
try:
    conobj = Mysql.connect(host="localhost",port ="3306",user="root", password = "Ramgup9393@")
    curobj = conobj.cursor()
    db = input("Enter the Database To create ")
    qry = f"Create database {db}"
    curobj.execute(qry)
    print("Database is Created Successfully ")
except Mysql.DatabaseError as e:
    print("Problem in Database ",e)
    