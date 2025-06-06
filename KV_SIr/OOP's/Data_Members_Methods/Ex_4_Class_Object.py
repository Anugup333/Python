# This file name and acts as module name 
class Student:
    def set_stud_values(self,sno,name,marks,cname="OUCET"):
        self.sno = sno
        self.name = name
        self.marks = marks
        self.cname = cname
    
    def dis_stu_data(self):
        pass
        print('='*50)
        print("Student Number ",self.sno)
        print("Student Name ",self.name)
        print("Student Marks ",self.marks)
        print("Student Course Name ",self.cname)
        print('='*50)