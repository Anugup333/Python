
import mysql.connector as Mysql
import sys
while True:
    try:
        conobj = Mysql.connect(host="localhost",port ="3306",user="root", password = "Ramgup9393@",database="bank")
        curobj = conobj.cursor() 
        ano = int(input(f"Enter Account Number "))    
        aname = input(f"Enter Customer Name ")    
        bal = float(input(f"Enter Customer Balance "))
        iq = f"insert into deposit values({ano},'{aname}',{bal})"
        curobj.execute(iq)  
        conobj.commit()
        print("Account Created Successfully ",curobj.rowcount)
        print('='*50)
        ch = input("Do you want to Create another Account (yes/no) ")
        if ch.lower()=='no':
            print("Thanks for Using this Program ")
            sys.exit()
            
    except Mysql.DatabaseError as e:
        print("Problem in Database ",e)
    