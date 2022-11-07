def rightrotation(arr,k):
    n=len(arr)
    while(k > 0):
        temp = arr[n-1]
        for i in range(n-1,0,-1):
            arr[i] = arr[i-1]
        arr[0] = temp
        k-=1
    return arr

def leftrotation(arr,k):
    n=len(arr)
    while(k > 0):
        temp = arr[0]
        for i in range(0,n-1):
            arr[i] = arr[i+1]
        arr[n-1] = temp
        k-=1
    return arr

def main():
    # No of test case
    t = int(input())
    while t>0:
        # n = length of list , k = no of times we want to rotate the Array
        n,k = map(int,input().split()) 
        # elements of array
        arr = [int(i) for i in input().split()]
        #print(f"Right Rotation for k ={k}: {rightrotation(arr,k)}")
        print(f"Left Rotation for k = {k}: {leftrotation(arr,k)}")
        t -= 1
if __name__ == "__main__":
    main()
