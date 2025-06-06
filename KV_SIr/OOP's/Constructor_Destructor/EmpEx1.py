class Employee:
    
    # Constructor
    def __init__(self):
        self.eno = int(input("Enter Employee Number : "))
        self.ename = input("Enter Employee Name : ")
        self.sal = float(input("Enter Employee Salary : "))
    
    def dis_emp_data(self):
        print('='*50)
        print("Employee Number ",self.eno)
        print("Employee Name ",self.ename)
        print("Employee Salary ",self.sal)
        print('='*50)


# main program 
eo = Employee()
eo.dis_emp_data()
