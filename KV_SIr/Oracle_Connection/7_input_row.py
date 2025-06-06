import oracledb as odb
try:
    conobj = odb.connect("system/1234@localhost/xe")
    curobj = conobj.cursor()
    # design the query    
    print("="*50)
    n = int(input("Enter the rows that insert "))
    for i in range(n):
        empno = int(input(f"Enter the Empno of {i+1} Employee "))    
        name = input(f"Enter the Name of {i+1} Employee ")    
        empsal = float(input(f"Enter the Salary of {i+1} Employee "))
        cname = input(f"Enter the comapany name of {i+1} employee ")
            
        qry = f"""insert into employee values({empno},'{name}',{empsal},'{cname}')"""
        curobj.execute(qry)
        conobj.commit()
        print("="*50)
        print(f"{i+1} Row inserted Successfully ")
        print("="*50)
    print("Thank you Using this ")
except odb.DatabaseError as e:
    print("Problem in the data",e)