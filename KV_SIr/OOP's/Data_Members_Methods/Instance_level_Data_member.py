class Employee:
    pass
e1 = Employee()

e1.sno = 100
e1.name = "Anuj"
e1.sal = 4.5
# This is Used to dispaly what Object Conatin 
print("="*50)
print("Content of e1 object of Employee : ",e1.__dict__)
print("Sno of Employee of e1 ",e1.sno)
print("Name of Employee of e1 ",e1.name)
print("Salary of Employee of e1 ",e1.sal)