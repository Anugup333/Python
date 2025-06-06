from college import College
class Student(College):
    def set_stu_det(self):
        self.sno = int(input("Enter Student Number : "))
        self.sname = input("Enter Student Name : ")
        self.marks = float(input("Enter Student Marks : "))
        
    
    def disp_stu_det(self):
        print("Student Details ")
        print("="*50)
        print("Student Number : ",self.sno)
        print("Student Name : ",self.sname)
        print("Student Marks : ",self.marks)
        print("="*50)
