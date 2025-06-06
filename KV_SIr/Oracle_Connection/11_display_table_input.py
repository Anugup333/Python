"""write a program which will accepts a table name 
and display all the records of the name and column name 
also"""

import oracledb as odb
def get_records():
    try:
        tname = input("Enter the Table name ")
        conobj =  odb.connect("system/1234@localhost/xe")
        curobj = conobj.cursor()
        curobj.execute(f"select * from {tname}")
        print('='*50)
        print(f"All the columns in that table {tname}")
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
        
        
    except odb.DatabaseError as e:
        print("Problem in the Database ",e)
    

get_records()