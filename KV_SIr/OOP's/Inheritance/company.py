class Company:
    def set_comp_det(self):
        self.cname = input("Enter Company Name : ")
        self.cplace = input("Enter Company Place : ")
    
    def disp_comp_det(self):
        print("Company Name : ",self.cname)
        print("Company Place : ",self.cplace)


