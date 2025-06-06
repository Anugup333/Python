# this program which we read from the employee table 
import oracledb as odb
try:
    conobj = odb.connect("system/1234@localhost/xe")
    curobj = conobj.cursor()
except odb.DatabaseError as e:
    print("Problem in the database ",e) 

def select_table():
    qry = "select * from employee"
    curobj.execute(qry)
    print('='*50)
    print("Employee details ")
    print("="*50) 
    
    # fetchone
    # while True:
    #     record = curobj.fetchone()
    #     if record != None: 
    #         for val in record:
    #             print(f"\t{val} ",end='')
    #         print()
    #     else:
    #         break
    
    # fetchamany()
    # records = curobj.fetchmany(4)
    # for record in records:
    #     for val in record:
    #         print(f"\t{val}",end="")
    #     print()
    # print("="*50)
    
    # fetchall()
    records = curobj.fetchall()
    for record in records:
        print(record)
    
    
    
select_table()