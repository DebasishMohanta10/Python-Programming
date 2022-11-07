n,m = map(int,input().split())
mat1 = []
for _ in range(n):
    mat1.append([int(i) for i in input().split()])
mat2 = []
for _ in range(n):
    mat2.append([int(i) for i in input().split()])

# Resultant Matrix
result = []
for _ in range(n):
    result.append([0]*m)
# Matrix Addition
for i in range(n):
    for j in range(m):
        result[i][j] = mat1[i][j] + mat2[i][j]

# Printing Resultant Matrix
print("Resultant Matrix is: ")
for i in range(n):
    for j in range(m):
        print(result[i][j],end=" ")
    print()
