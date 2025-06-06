class Employee:
    
    @classmethod
    def get_com_ceo(cls):
        cls.ceo = "Rajat Patidar"
    
    @classmethod
    def get_com_data(cls):
        cls.cname = "IBM"
        # call Class level method inside the class level method
        cls.get_com_add()
    
    @classmethod
    def get_com_add(cls):
        cls.addr = "HYD" 
               
    def get_emp_data(self):
        self.eno = int(input("Enter Employee Number : "))
        self.ename = input("Enter Employee Name : ")
    
    def dis_emp_data(self):
        print("="*50)
        print("Employee Number ",self.eno)
        print("Employee Name ",self.ename)
        print("Company Name : ",Employee.cname)
        print("Company Address : ",self.addr)
        # we can call class level method inside instance method
        self.get_com_ceo()
        print("Company Ceo : ",self.ceo)
        print("="*50)
    
        
# main program 
e1 = Employee()
Employee.get_com_data()
e1.get_emp_data()
e1.dis_emp_data()

