# This program is used to insert the employee value in the Table Employee

import oracledb 

class InsertEmployeeData:
    
    def get_data(self):
        self.eno = int(input("Enter Employee Number : "))
        self.ename = input("Enter Employee Name : ")
        self.esal = float(input("Enter Employee Salary : "))
        self.cname = input("Enter Employee Company Name : ")
    
    def insert_data(self):
        self.get_data()
        try:
            conobj = oracledb.connect("system/1234@localhost/xe")
            curobj = conobj.cursor()
            qry = f"insert into employee values({self.eno},'{self.ename}',{self.esal},'{self.cname}')"
            curobj.execute(qry)
            if curobj.rowcount >0:
                print("Insert the data Successfully") 
                conobj.commit()
            else:
                print("Unable To Insert Into the Table")
        except oracledb.DatabaseError as e:
            print("Problem in the Databse ",e)

# main program
i = InsertEmployeeData()
i.insert_data()
        