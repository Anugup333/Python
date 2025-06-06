# This program reads and insert student into the student.txt 
# Using Picking Module
import pickle,sys
from Ex_4_Class_Object import Student
class StudentPickle:
    def insert_data(self):
        with open("student.txt",'ab') as fp:
            while True:
                try:
                    self.sno = int(input("Enter Student Number : "))
                    self.name = input("Enter Student Name : ")
                    self.marks = float(input("Enter Student Marks : "))    
                    so = Student()
                    so.set_stud_values(self.sno,self.name,self.marks)
                    # dump or save the Student data in file
                    pickle.dump(so,fp)
                    print("="*50)
                    print("Student Record Inserted into the file Successfully...")
                    print("="*50)
                    ch = input("Do you want to insert another record(yes/no): ")
                    if ch.lower() == "no":
                        print("Thanks for using the Program")
                        sys.exit()
                except ValueError:
                    print("Don't Enter str/symbols for numeric value  ")
    
# main Program 
s = StudentPickle()
s.insert_data()