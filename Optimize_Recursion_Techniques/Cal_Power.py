class Recursion:
    def calcPower(self,x,n):
        if n == 0:
            return 1
        if x == 0:
            return 0
        return x * self.calcPower(x,n-1)
    
    def opt_calcPower(self,x,n):  # Optimize Technique
        
        if n == 0:      # Base Case 1 
            return 1
        if x == 0:     # Base Case 2
            return 0
        if n % 2 == 0:  # When n is Even 
            return self.opt_calcPower(x,n//2) * self.opt_calcPower(x,n//2)
        else:          # When n is Odd 
            return self.opt_calcPower(x,n//2) * self.opt_calcPower(x,n//2) * x
        

re = Recursion()
x = int(input("Enter the number that power uou want : "))
n = int(input("Enter the power : "))
re = Recursion()
print(f"{x} to the power {n} is {re.opt_calcPower(x,n)}")