# Maximum sum of k consecutive elements in an array of length n
# Sliding Window Technique
# Used to reduce the no of operation in an array
# specially used in case of subarray problems

n,k = map(int,input().split())
arr = [int(i) for i in input().split()]
sum = 0
for i in range(k):
    sum += arr[i]
max = sum
for j in range(k,n):
    max = max - arr[j-k] + arr[j]
    if sum < max:
        sum = max
print(sum)