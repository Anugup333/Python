'''  Date- 28/01/2024
     Complex Arithmatic                 '''

class ComplexNumbers:
    def __init__(self,a,b,c,d):
        self.a =a
        self.b =b
        self.c = c
        self.d = d
    
    def plus(self):
        real = self.a +self.c
        img = self.b + self.d
        print(real,end="")
        print(" +","i",end="")
        print(img)
    
    def multiply(self):
        real = self.a*self.c - self.b*self.d
        img = self.a*self.d + self.b*self.c
        print(real,end="")
        print(" +","i",end="")
        print(img)

a,b = map(int,input().split())
c,d = map(int,input().split())
flag = int(input())
com = ComplexNumbers(a,b,c,d)
if flag ==1:
    com.plus()
elif flag == 2:
    com.multiply()
else:
    print("")
