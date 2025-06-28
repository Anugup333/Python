'''
    
        42. Trapping Rain Water
            
            Given n non-negative integers representing an elevation map where the width of each bar is 1, 
            compute how much water it can trap after raining.
            
            Example 1:

            Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
            Output: 6
            Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
            
            Example 2:

            Input: height = [4,2,0,3,2,5]
            Output: 9
'''
from typing import List

class Solution:
    def get_left_max(self,height,n):
        left_max = [0]*n
        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],height[i])
        return left_max
    
    def get_right_max(self,height,n):
        right_max = [0]*n
        right_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i])
        return right_max
    
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        left_max = self.get_left_max(height,n)
        right_max = self.get_right_max(height,n)

        water = 0

        for i in range(n):
            h = min(left_max[i],right_max[i]) - height[i]

            water +=h
        
        return water 
        