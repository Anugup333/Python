# This program is updated sa and company name based employee number
import oracledb as odb
try:
    conobj = odb.connect("system/1234@localhost/xe")
    curobj = conobj.cursor()
except odb.DatabaseError as e:
    print("Problem in the database ",e) 

def update_table():
    # accept employee number , sal, and company name
    empno = int(input("Enter the employee NO "))
    empsal = float(input("Enter the Employee salary for updation "))
    empcname = input("Enter the Company Name ")
    curobj.execute(f"update employee set sal = {empsal}, cname = '{empcname}' where eno = {empno}")
    conobj.commit()
    if curobj.rowcount >0:
        print("Employee Record Updated ")
    else:
        print("Employee Record does not exists")

update_table()
    