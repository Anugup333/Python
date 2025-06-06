class Human:
    @staticmethod
    def dispdata(obj):
        print('='*50)
        for k,v in obj.__dict__.items():
            print(f"{k} ----> {v}")


# main program 
emp = Human()
stu = Human()
tea = Human()

# add data to the emp object
emp.eno = 10
emp.name = "Akash"
emp.sal = 4.5

# add data to stu object
stu.sno = 11
stu.name = "Anuj"
stu.sal = 0

# add the data to tea object
tea.tno = 12
tea.name = "Shobha"
tea.sal = 7.0


print("="*50)
Human.dispdata(emp)
print("="*50)
Human.dispdata(stu)
print("="*50)
Human.dispdata(tea)