''''
Rotate by 90 degree

        
        Given a square mat[][]. The task is to rotate it by 90 degrees in clockwise direction without using any extra space.

        Examples:

        Input: mat[][] = [[1 2 3], [4 5 6], [7 8 9]]
        Output:
        7 4 1 
        8 5 2
        9 6 3
        
        Input: mat[][] = [1 2], [3 4]
        Output:
        3 1 
        4 2
        
        Input: mat[][] = [[1]]
        Output:
        1
'''


#User function Template for python3

def rotate(mat): 
    #code here
    m = len(mat)
    n = len(mat[0])

    
    # transpose 
    for i in range(m):
        for j in range(i,n):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]      
    
    # reverse each row in that 
    
    for i in range(m):
        mat[i] = mat[i][::-1]
    
    
mat = [[1,2,3],[4,5,6],[7,8,9]]

rotate(mat)

print(mat)
