class Student:
    # define class level Data member
    college = "Jss"

Student.address = "Noida Sector 62"

# both are Called Class level Data members
s1 = Student()

# Access the Class level Data Members 
print("Student Collge Name of s1 : ",s1.college)
print("Student College Address : ",Student.address)