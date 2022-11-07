def reverseRightAlgo(arr,i,j):
    while(i < j):
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1

def printArr(arr,n):
    for i in range(n):
        print(arr[i],end= " ")

def main():
    t = int(input())
    while t>0:
        n,k = map(int,input().split())
        arr = [int(i) for i in input().split()]
        reverseRightAlgo(arr,n-k,n-1)
        reverseRightAlgo(arr,0,n-k-1)
        reverseRightAlgo(arr,0,n-1)
        printArr(arr,n)
        t -= 1

if __name__ == "__main__":
    main()