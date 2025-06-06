"""write a program which will accepts a table name 
and display all the records of the name and column name 
also"""

import mysql.connector as Mysql
def get_records():
    try:
        
        conobj = Mysql.connect(host="localhost",port ="3306",user="root", password = "Ramgup9393@",database="kvr_db")
        curobj = conobj.cursor()
        tname = input("Enter the Table name ") 
        curobj.execute(f"select * from {tname}")
        print('='*50)
        print(f"All the Rows in that table {tname}")
        print('='*50)
        for colname in [metadata for metadata in curobj.description]:
            print(f"{colname[0]}\t",end="")
        print()
        print('='*50)
        records = curobj.fetchall()
        for record in records:
            for val in record:
                print(f"{val}\t",end="")
            print()
        print('='*50)
        
        
    except Mysql.DatabaseError as e:
        print("Problem in the Database ",e)
    

get_records()