class Recursion:
    def printFib(self,a,b,n):
        if n == 0:
            return
        c = a + b
        print(c,end="\t")
        self.printFib(b,c,n-1)
        

re = Recursion()
n = int(input("Enter the term that you want to print : "))
a = 0  
b = 1
print(a,end="\t")
print(b,end="\t") 
re.printFib(a,b,n - 2)