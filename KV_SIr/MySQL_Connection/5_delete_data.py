# This i used to delete  data in the data base

import mysql.connector as Mysql
import sys
while True:
    try:
        conobj = Mysql.connect(host="localhost",port ="3306",user="root", password = "Ramgup9393@",database="kvr_db")
        curobj = conobj.cursor() 
        empno = int(input("Enter the Employee Number: "))
        iq = f"delete from employee where eno = {empno}"
        curobj.execute(iq)  
        conobj.commit()
        if curobj.rowcount>0:
            print("Record Deleted Successfully in Table ")
        else:
            print("Employee Record Does not Exists")
        print('='*50)
        ch = input("Do you want to insert another record(yes/no) ")
        if ch.lower()=='no':
            print("Thanks for Using this Program ")
            sys.exit()
            
    except Mysql.DatabaseError as e:
        print("Problem in Database ",e)
    