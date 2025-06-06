# This Program Reads all the records of Employee 
# Table and Display it by using the Class

import oracledb 

class EmployeeRecords:
    def getrecords(self):
        conobj = oracledb.connect("system/1234@localhost/xe")
        curobj = conobj.cursor()
        qry = "select * from employee"
        curobj.execute(qry)
        print("Display The Records of Employee Table ")
        print("="*50)
        for col in [metadata for metadata in curobj.description]:
            print(f"\t{col[0]}",end="")
        print()
        print('='*50)
        records = curobj.fetchall()
        for record in records:
            for val in record:
                print(f"\t{val}",end="")
            print()
        print("="*50)
        


# main Program 
eo = EmployeeRecords()
eo.getrecords()