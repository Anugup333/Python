'''
    Factorials of large numbers

        Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.

            Examples:

            Input: n = 5
            Output: [1, 2, 0]
            Explanation: 5! = 1*2*3*4*5 = 120
            
            Input: n = 10
            Output: [3, 6, 2, 8, 8, 0, 0]
            Explanation: 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800
            
            Input: n = 1
            Output: [1]
            Explanation: 1! = 1 
'''

#User function Template for python3

class Solution:
    def factorial(self, n):
        #code here
        self.ans = [1]
        for multiplier in range(2,n+1):
            self.multiply(multiplier)
        
        return self.ans[::-1]
    

    def multiply(self,multiplier):
        print(len(self.ans))
        carry = 0
        for i in range(len(self.ans)):
            res = multiplier * self.ans[i]
            res += carry 
            res = res % 10
            carry = res // 10
        
        while carry > 0:
            self.ans.append(carry % 10)
            carry = carry // 10  
        print(self.ans)

    
    
    

if __name__ == "__main__":
    s = Solution()
    print(s.factorial(5))

                