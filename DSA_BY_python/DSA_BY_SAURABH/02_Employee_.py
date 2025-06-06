class Employee:
    def __init__(self,empid=None,name=None,salary=None) -> None:
        self.empid = empid
        self.name = name
        self.salary = salary
    def set_Empid(self,empid):
        self.empid = empid
    def set_Name(self,name):
        self.name = name
    def set_Salary(self,salary):
        self.salary = salary
    def get_Empid(self):
        return self.empid
    def get_Name(self):
        return self.name
    def get_Salary(self):
        return self.salary

e1 = Employee()
e2 = Employee(1,"Rahul",40000)
e1.set_Empid(2)
e1.set_Name("Romesh")
e1.set_Salary(50000)

print(e1.get_Empid())
print(e1.get_Name())
print(e1.get_Salary())
print(e2.get_Empid())
print(e2.get_Name())
print(e2.get_Salary())