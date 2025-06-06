class GrandParent:
    def getGrandParentProp(self):
        gpp=float(input("Enter Grand Parent Property:"))
        return gpp

class Parent(GrandParent):
    def getParentProp(self):
        pp=float(input("Enter Parent Property:"))
        return pp

class Child(Parent):
    def getChildProperty(self):
        cp=float(input("Enter Child Property:"))
        return cp

    def getTotalProp(self):
        gpp=self.getGrandParentProp()
        pp=self.getParentProp()
        cp=self.getChildProperty()
        tp=gpp+pp+cp
        print("Parent Grand Property={}".format(gpp))
        print("Parent Property={}".format(pp))
        print("Child Property={}".format(cp))
        print("Total Property={}".format(tp))


#main Program
co=Child()
co.getTotalProp()