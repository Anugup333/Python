class Banking:  # Here Banking is called Abstract Class 
    def openac(self):pass  # Null Body Methods
    def deposit(self):pass
    def loan(self):pass

class Ravi(Banking):
    def openac(self):
        print("Ravi Opened Saving Account in SBi")
        
class Person(Banking):
    def loan(self,name,lamt):
        print("{} Taken {} as Loan and went out of India".format(name,lamt))
        
# main program 
r = Ravi()
r.openac()
p = Person()
p.loan("VMalya",2.3)
p.loan("Nmodi",4.5)
