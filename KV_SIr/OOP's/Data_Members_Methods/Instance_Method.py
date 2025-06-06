# Program for reading and Writing the Student Details

class Student:
    # Instance Method
    def read_stu_data(self):
        print("="*50)
        self.sno = int(input("Enter Student Number: "))
        self.name = input("Enter Student Name: ")
        self.marks = float(input("Enter Student Marks: "))
        print("="*50)
    
    # Instance Method
    def disp_stu_data(self):
        print("="*50)
        print("Student Number ",self.sno)
        print("Student Name ",self.name)
        print("Student Marks ",self.marks)
        print("="*50)

s1 = Student()
s2 = Student()

print("="*50)
print("Enter the First Student Information ")
s1.read_stu_data()
print("="*50)
print("Enter the Second Student Information ")
s2.read_stu_data()
print("="*50)
print("First Student Information")
s1.disp_stu_data()
print("="*50)
print("Second Student Information")
s2.disp_stu_data()