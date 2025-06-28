m = int(input())
n = int(input())
matrix = [list(map(int,input().split())) for i in range(m) ]
print(matrix)
ans = []
for i in range(n):
    if i%2==0:
        ans.extend([matrix[j][i] for j in range(m)])
    else:
        ans.extend([matrix[m-j-1][i] for j in range(m)])
print(ans)