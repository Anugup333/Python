# This Code is used to update the datai database 

import mysql.connector as Mysql
import sys
while True:
    try:
        conobj = Mysql.connect(host="localhost",port ="3306",user="root", password = "Ramgup9393@",database="kvr_db")
        curobj = conobj.cursor() 
        print("Update the Record of the Employee ")
        empno = int(input(f"Enter Employee Number "))    
        hike = float(input(f"Enter the Hike percentage "))
        iq = f"update employee set esal = esal+esal*{hike/100} where eno = {empno}"
        curobj.execute(iq)  
        conobj.commit()
        print("Record Updated Successfully in Table ",curobj.rowcount)
        print('='*50)
        ch = input("Do you want to updated another record(yes/no) ")
        if ch.lower()=='no':
            print("Thanks for Using this Program ")
            sys.exit()
            
    except Mysql.DatabaseError as e:
        print("Problem in Database ",e)
    