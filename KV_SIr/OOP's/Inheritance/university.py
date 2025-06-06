class University:
    def set_univ_det(self):
        self.uname = input("Enter University Name : ")
        self.uloc = input("Enter University Location : ")
    
    def disp_univ_det(self):
        print("University Details")
        print("="*50)
        print("University Name : ",self.uname)
        print("University Location : ",self.uloc)
        print("="*50)
        
