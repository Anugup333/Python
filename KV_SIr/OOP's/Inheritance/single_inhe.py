class Parent:
    def getParentProp(self):
        self.pp=float(input("Enter Parent Property:"))

class Child(Parent):
    def getChildProperty(self):
        self.cp=float(input("Enter Child Property:"))
    def getTotalProp(self):
        self.tp=self.pp+self.cp
        print("Parent Property={}".format(self.pp))
        print("Child Property={}".format(self.cp))
        print("Total Property={}".format(self.tp))


#main Program
co=Child()
co.getParentProp()
co.getChildProperty()
co.getTotalProp()
