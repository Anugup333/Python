# Write a Program is used to print the table of a number 

class Table:
    def getnumber(self):
        self.num = int(input("Enter the Number : "))
            
    def print_table(self):
        self.getnumber()
        if(self.num > 0):
            print(f"Multiplication Table of {self.num}")
            print("="*50)
            for i in range(1,11):
                print(f"{i} * {self.num} = {self.num*i}")
            print("="*50)
        else:
            print(f"{self.num} is Invalid Input ")


# main program 
t = Table()
t.print_table()