'''
        15. 3Sum
            
            Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
            and j != k, and nums[i] + nums[j] + nums[k] == 0.

            Notice that the solution set must not contain duplicate triplets.
            
            Example 1:

            Input: nums = [-1,0,1,2,-1,-4]
            Output: [[-1,-1,2],[-1,0,1]]
            Explanation: 
            nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
            nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
            nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
            The distinct triplets are [-1,0,1] and [-1,-1,2].
            Notice that the order of the output and the order of the triplets does not matter.
            
            Example 2:

            Input: nums = [0,1,1]
            Output: []
            Explanation: The only possible triplet does not sum up to 0.
            
            Example 3:

            Input: nums = [0,0,0]
            Output: [[0,0,0]]
            Explanation: The only possible triplet sums up to 0.

'''
from typing import List

class Solution:

    def twosum(self,nums,target,start,end):
        while start < end:
            if nums[start] + nums[end] < target:
                start +=1
            elif nums[start] + nums[end] > target:
                end -=1
            else:
                # first we remove duplicates from either end (start,end)

                while start < end and nums[start] == nums[start+1]:
                    start +=1
                while start < end and nums[end]  == nums[end-1]:
                    end -=1

                self.result.append([-target,nums[start],nums[end]])

                start +=1
                end -=1 

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []

        self.result = []

        # Sort 
        nums.sort()

        for i in range(n-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            n1 = nums[i]
            target = -n1

            self.twosum(nums,target,i+1,n-1)  # it will be find (n1,n2,n3) = 0
    
        return self.result 
        