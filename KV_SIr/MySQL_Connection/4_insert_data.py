# This pcode accepts employee data and insert in the table 
import mysql.connector as Mysql
import sys
while True:
    try:
        conobj = Mysql.connect(host="localhost",port ="3306",user="root", password = "Ramgup9393@",database="kvr_db")
        curobj = conobj.cursor() 
        empno = int(input(f"Enter Employee Number "))    
        empname = input(f"Enter Employee Name ")    
        empsal = float(input(f"Enter Employee Salary "))
        iq = f"insert into employee values({empno},'{empname}',{empsal})"
        curobj.execute(iq)  
        conobj.commit()
        print("Record Inserted Successfully in Table ",curobj.rowcount)
        print('='*50)
        ch = input("Do you want to insert another record(yes/no) ")
        if ch.lower()=='no':
            print("Thanks for Using this Program ")
            sys.exit()
            
    except Mysql.DatabaseError as e:
        print("Problem in Database ",e)
    