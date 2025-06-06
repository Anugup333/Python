from university import University

class College(University):
    
    def set_coll_det(self):
        self.cname = input("Enter College Name : ")
        self.cloc = input("Enter College Location : ")
    
    def disp_coll_det(self):
        print("College Details")
        print("="*50)
        print("College Name : ",self.cname)
        print("College Location : ",self.cloc)
        print("="*50)