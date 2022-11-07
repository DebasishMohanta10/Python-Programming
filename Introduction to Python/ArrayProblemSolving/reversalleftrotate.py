# Left Rotation using Reversal Algorithm
# -> Reverse(0,k-1)
# -> Reverse(k,n-1)
# -> Reverse(0,n-1)
def leftRotate(arr,i,j):
    while(j>i):
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
def printArr(arr,n):
    for i in range(n):
        print(arr[i],end=" ")

def main():
    t = int(input())
    while t>0:
        n,k = map(int,input().split())
        arr = [int(i) for i in input().split()]
        leftRotate(arr,0,k-1)
        leftRotate(arr,k,n-1)
        leftRotate(arr,0,n-1)
        printArr(arr,n)
        t -= 1

if __name__ == "__main__":
    main()
