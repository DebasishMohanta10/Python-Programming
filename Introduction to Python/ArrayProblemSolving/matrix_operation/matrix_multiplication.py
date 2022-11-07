a,b = map(int,input().split())
mat1 = []
for _ in range(a):
    mat1.append([int(i) for i in input().split()])

n,m = map(int,input().split())
mat2 = []
for _ in range(n):
    mat2.append([int(i) for i in input().split()])

if b == n:
    result = []
    for _ in range(a):
        result.append([0]*m)
    
    for i in range(a):
        for j in range(m):
            for k in range(m):
                result[i][j] += mat1[i][k] * mat2[k][j]
    # printing the matrix
    print("The reultant Matrix is: ")
    for i in range(a):
        for j in range(m):
            print(result[i][j],end=" ")
        print()
else:
    print("Matrix Multiplication Not possible.")


