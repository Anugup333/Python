'''

Container With Most Water

        Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the vertical lines, find the maximum amount of water that can be contained between any two lines, together with the x-axis.

        Note: In the case of a single vertical line it will not be able to hold water.

        Examples:

        Input: arr[] = [1, 5, 4, 3]
        Output: 6
        Explanation: 5 and 3 are 2 distance apart. So the size of the base is 2. Height of container = min(5, 3) = 3. So, total area to hold water = 3 * 2 = 6.
        
        Input: arr[] = [3, 1, 2, 4, 5]
        Output: 12
        Explanation: 5 and 3 are 4 distance apart. So the size of the base is 4. Height of container = min(5, 3) = 3. So, total area to hold water = 4 * 3 = 12.
        
        Input: arr[] = [2, 1, 8, 6, 4, 6, 5, 5]
        Output: 25 
'''

class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        
        start = 0
        end = n-1
        max_water = 0
        
        while start < end:
            width = end-start
            height = min(arr[start],arr[end])
            area  = width * height
            max_water = max(area,max_water)
                
            if arr[start] < arr[end]:
                start +=1
            else:
                end -=1
        
        return max_water
                    
               