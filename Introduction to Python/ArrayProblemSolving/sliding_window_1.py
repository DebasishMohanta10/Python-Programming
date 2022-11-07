# Maximum sum of k consecutive elements in an array of length n
n,k = map(int,input().split())
arr = [int(i) for i in input().split()]
sum = 0
for i in range(n):
    sum1 = 0
    if i+k <= n:
        for j in range(i,i+k):
            sum1 += arr[j]
        if sum1 > sum:
            sum = sum1
    

print(sum)