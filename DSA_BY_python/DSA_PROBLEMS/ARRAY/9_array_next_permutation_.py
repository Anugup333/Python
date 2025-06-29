'''
Next Permutation

        Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

        Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

        Examples:

        Input: arr = [2, 4, 1, 7, 5, 0]
        Output: [2, 4, 5, 0, 1, 7]
        Explanation: The next permutation of the given array is {2, 4, 5, 0, 1, 7}.
        
        Input: arr = [3, 2, 1]
        Output: [1, 2, 3]
        Explanation: As arr[] is the last permutation, the next permutation is the lowest one.
        
        Input: arr = [3, 4, 2, 5, 1]
        Output: [3, 4, 5, 1, 2]
        Explanation: The next permutation of the given array is [3, 4, 5, 1, 2].
'''

class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        
        # first find the black gola 
        gola_index = -1
        
        for i in range(n-1,-1,-1):
            if arr[i] > arr[i-1]:
                gola_index = i-1 
                break
        
        # find the just bada from the right
        if gola_index != -1:
            swap_index = gola_index
            for i in range(n-1,gola_index,-1):
                if arr[i] > arr[gola_index]:
                    swap_index = i 
                    break
            
            # swap it with the just bada elemnt from the right
            
            arr[gola_index], arr[swap_index] = arr[swap_index],arr[gola_index]
        
        arr[gola_index+1:] =  arr[gola_index+1:][::-1] 