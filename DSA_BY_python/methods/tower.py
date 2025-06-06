def towerOfHanoi(n):
    # Write your code here
    # Return a 2-D array
    ans = list()
    def hanoi(n,s,h,d):
        if n == 1:
            ans.append([s,d])
            return 
        hanoi(n-1,s,d,h)
        ans.append([s,d])
        hanoi(n-1,h,s,d)
    
    hanoi(n,1,2,3)
    return ans

n = 3
print(towerOfHanoi(n))