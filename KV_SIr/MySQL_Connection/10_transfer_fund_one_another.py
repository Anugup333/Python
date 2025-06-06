# This Program is used to transfer the fund to another 

import mysql.connector as Mysql
import sys

try:
    conobj = Mysql.connect(host="localhost",port ="3306",user="root", password = "Ramgup9393@",database="bank")
    curobj = conobj.cursor() 
    # get all account deatils
    curobj.execute("Select * from deposit")
    records = curobj.fetchall()
    print('='*50)
    for colname in [metadata for metadata in curobj.description]:
        print(f"\t {colname[0]}",end="")
    print()
    print('='*50)
    for record in records:
        for val in record:
            print(f"\t {val}",end="")
        print()
    print('='*50)
    
    scacno = int(input("Enter Source Account Number : "))
    found = False
    srbal = 0
    for record in records:
        if record[0] == scacno:
            found = True
            srbal = record[2]
            break
    if found == False:
        print('='*50)
        print(f"{scacno} is Invalid Account Number: ")
        print('='*50)
    else:
        srcamt = float(input("Enter the Ammount to  transfer to source Account: "))
        if (srcamt+500)>srbal:
            print('='*50)
            print("Source Account does not contain sufficient funds : ")
            print('='*50)
        else:
            desacno = int(input("Enter Destination Account Number : "))
            found = False
            desbal = 0
            for record in records:
                if record[0] == desacno:
                    found = True
                    desbal = record[2]
                    break
            if found == False:
                print('='*50)
                print(f"{desacno} is Invalid Destination Account Number ")
                print('='*50)
            else:
                # update the account 
                curobj.execute(f"Update deposit set bal = bal - {srcamt} where acno = {scacno}")
                curobj.execute(f"Update deposit set bal = bal + {srcamt} where acno = {desacno}")
                conobj.commit()
                print("="*50)
                print(f"From {scacno} Account Number , INR {srcamt} Transfered into Account {desacno}")
                print("="*50)
                curobj.execute("Select * from deposit")
                records = curobj.fetchall()
                print('='*50)
                for colname in [metadata for metadata in curobj.description]:
                    print(f"\t {colname[0]}",end="")
                print()
                print('='*50)
                for record in records:
                    for val in record:
                        print(f"\t {val}",end="")
                    print()
                print('='*50)  
            
except Mysql.DatabaseError as e:
    print("Problem in Database ",e)
    