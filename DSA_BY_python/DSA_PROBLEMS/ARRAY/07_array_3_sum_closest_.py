'''
    16. 3Sum Closest
    
            Given an integer array nums of length n and an integer target, 
            find three integers in nums such that the sum is closest to target.
            Return the sum of the three integers.
            You may assume that each input would have exactly one solution.

            Example 1:
            Input: nums = [-1,2,1,-4], target = 1
            Output: 2
            Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
            
            Example 2:
            Input: nums = [0,0,0], target = 1
            Output: 0
            Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        closest_sum = float("inf")
        nums.sort()
        for i in range(n-2):
            start = i+1
            end = n-1
            while start < end:
                curr_sum = nums[i] + nums[start] + nums[end]
                if abs(target - curr_sum ) < abs(target - closest_sum):
                    closest_sum = curr_sum
                
                if curr_sum < target:
                    start +=1
                else:
                    end -=1 
        return closest_sum
