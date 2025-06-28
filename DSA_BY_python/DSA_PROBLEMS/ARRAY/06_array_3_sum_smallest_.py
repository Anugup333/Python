"""
                                     3 Sum Smaller

        Given an array of n integers nums and a target, find the number of index triplets i,
        j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

        For example, given nums = [-2, 0, 1, 3], and target = 2.
        
        Return 2. Because there are two triplets which sums are less than 2:
        
        [-2, 0, 1] [-2, 0, 3]
        
        URL: https://leetcode.com/problems/3sum-smaller/
    
    """ 

class Solution(object):

    def threeSumSmaller(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: int
        """
        n = len(nums)
        if n <=3:
            return len([])

        count = 0
        nums = sorted(nums)

        for i in range(n-2):
            start = i + 1
            end = n -1
            while start < end:
                curr_sum  = nums[i] + nums[start] + nums[end]
                if  curr_sum < target:
                    count += end - start
                    start +=1
                else:
                    end -=1
        return count


if __name__ == "__main__":
    soln = Solution()
    print(soln.threeSumSmaller([3,1,0,-2], 4))