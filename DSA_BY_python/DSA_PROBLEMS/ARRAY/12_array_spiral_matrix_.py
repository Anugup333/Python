'''
    54. Spiral Matrix

        Given an m x n matrix, return all elements of the matrix in spiral order.

        Example 1:
        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [1,2,3,6,9,8,7,4,5]
        
        Example 2:
        Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)  # row 
        n = len(matrix[0])  # column

        top = 0 
        down = m-1

        left = 0
        right = n-1

        d = 0

        ''' 
            direction = 0  : left to right 
            direction = 1  : top to down 
            direction = 2  : right to left 
            direction = 3  : down to top 
        '''

        ans = []

        while(top <= down and left <= right):

            if d == 0:
                # left to right 
                # constant (row) (top) 
                for i in range(left,right+1):
                    ans.append(matrix[top][i])

                top +=1

            if d == 1:
                # top to down 
                # constant (column) (right) 
                for i in range(top,down+1):
                    ans.append(matrix[i][right])

                right -=1
            
            if d == 2:
                # right to left 
                # constant (row) (down)
                for i in range(right,left-1,-1):
                    ans.append(matrix[down][i])
                
                down -=1

            if d == 3:
                # down to top 
                # constant (column) (left)
                for i in range(down,top-1,-1):
                    ans.append(matrix[i][left])

                left +=1

            d +=1

            if d == 4:
                d = 0 
        
        
        
        return ans