from company import Company

class Employee(Company):
    def set_emp_det(self):
        self.eno = int(input("Enter Employee Number : "))
        self.ename = input("Enter Employee Name : ")
        self.esal = float(input("Enter Employee Salary : "))
        self.set_comp_det()
    
    def disp_emp_det(self):
        print("Employee Number : ",self.eno)
        print("Employee Name : ",self.ename)
        print("Employee Salary : ",self.esal)
        self.disp_comp_det()
