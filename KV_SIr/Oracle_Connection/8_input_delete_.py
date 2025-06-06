# ths program is used to delete the record from input taken
import oracledb as odb
conobj = odb.connect("system/1234@localhost/xe")
curobj = conobj.cursor()

def display_records():
    qry = "select * from employee"
    curobj.execute(qry)
    # get the data from query
    print("Data of the Table ")
    print("="*50)
    while True:
        record = curobj.fetchone()
        if record != None:
            for i in record:
                print(f"\t{i}",end="")
            print()
        else:
            break
    print('='*50)

def delete_employee():
    eno = int(input("Enter Employee number "))
    curobj.execute(f"delete from employee where eno = {eno}")
    if curobj.rowcount >0:
        print("Employee Record Removed ")
        conobj.commit()
    else:
        print("Employee Record does not exists")

display_records()     
delete_employee()
