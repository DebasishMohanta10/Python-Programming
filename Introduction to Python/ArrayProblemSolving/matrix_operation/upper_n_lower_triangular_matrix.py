def upperTriangular(mat,m,n):
    upTri =[]
    for i in range(m):
        upTri.append([0]*n)
    for i in range(m):
        for j in range(n):
            if i > j:
                upTri[i][j] = 0
            else:
                upTri[i][j] = mat[i][j]
    return upTri

def lowerTriangular(mat,m,n):
    lowTri = []
    for i in range(m):
        lowTri.append([0]*n)
    for i in range(m):
        for j in range(n):
            if j > i:
                lowTri[i][j] = 0
            else:
                lowTri[i][j] = mat[i][j]
    return lowTri

def printMat(mat,m,n):
    for i in range(m):
        for j in range(n):
            print(mat[i][j],end = " ")
        print()


def main():
    m,n = map(int,input().split())
    mat1 = []
    for i in range(m):
        mat1.append([int(i) for i in input().split()])
    lowerTri = lowerTriangular(mat1,m,n)
    printMat(lowerTri,m,n)
    upperTri = upperTriangular(mat1,m,n)
    printMat(upperTri,m,n)

if __name__ == "__main__":
    main()
