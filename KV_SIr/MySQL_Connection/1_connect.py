# This program obtaoins connection of the Mysql database 

import mysql.connector as Mysql
try:
    conobj = Mysql.connect(host="localhost",port ="3306",user="root", password = "Ramgup9393@")
    print("Type of Mysql Connection = ",type(conobj))
    print("Python Mysql Connection is established ")
except Mysql.DatabaseError as e:
    print("Problem in Database ",e)
    