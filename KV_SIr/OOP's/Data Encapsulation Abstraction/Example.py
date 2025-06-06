# WAP which will accept Student no,name and marks in three subjets
# Calculate the total marks 
# give the grade as fail 
# student secure less than 40 in any of three subjects
# Give the grade as distinction provided the total marks lies between 250 and 300
# Give the grade first provide the total 200 and 249
# Give the grade second provide the total 150 and 199
# Give the grade third provide the total 120 and 149
# generate the result and store it in the database 
# store (stnom,stname,sub1,sub2,sub3,total,grade)


# Implement this with classes and objects
import mysql.connector as sql

class Student:
    def __init__(self):
        self.srollno = int(input("Enter student Roll no : "))
        self.sname = input("Enter Student Name : ")
        print("Enter the Marks of the Subjects ")
        while True:
            self.sub1 = float(input("Enter First Subject Marks : "))
            if self.sub1 <= 100 and self.sub1>=0:
                break
        while True:
            self.sub2 = float(input("Enter Second Subject Marks : "))
            if self.sub2 <= 100 and self.sub2>=0:
                break
        while True:
            self.sub3 = float(input("Enter Third Subject Marks : "))
            if self.sub3 <= 100 and self.sub3 >=0:
                break
        
    def decide_result(self):
        self.total = self.sub1 + self.sub2 + self.sub3
        self.percent = (self.total)/3
        if self.sub1 < 40 or self.sub2 < 40 or self.sub3 < 40:
            self.grade = "FAIL"
        else:
            if self.total >= 120 and self.total <= 149:
                self.grade = "THIRD"
            elif self.total >= 150 and self.total <= 199:
                self.grade = "SECOND"
            elif self.total >= 200 and self.total <= 249:
                self.grade = "FIRST"
            else:
                self.grade= "DISTINCTION"
    
    
    def storeindb(self):
        try:
            conobj = sql.connect(host='localhost',user='root',password='Ramgup9393@',database='generaldb')
            curobj = conobj.cursor()
            qry = f"insert into result values({self.srollno},'{self.sname}',{self.sub1},{self.sub2},{self.sub3},{self.total},{self.percent},'{self.grade}')"
            curobj.execute(qry)
            conobj.commit()
            print("Student Record is inserted Succesfully! ")
        except sql.DatabaseError as e:
            print("Problem in database : ",e)

so = Student()

# print(so.__dict__)
so.decide_result()
# print(so.__dict__)

so.storeindb()