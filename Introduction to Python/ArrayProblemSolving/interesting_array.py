# Interesting Array
# PrepBuddy wants you to solve an interesting problem. You will discover an interesting technique while solving this problem.
# You are given an array of 
# N
# N integers in ascending order and a number 
# N
# N. You have to print indexes of two numbers in the array such that the sum equals to number 
# K
# K. In case no such pair exists print "no answer"(without quotes).

t = int(input())
while t > 0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    k =int(input())
    flag = 0
    # Two pointer technique (it works on sorted Array)
    i = 0
    j=len(arr)-1
    while(j>i):
        sum = arr[i] + arr[j]
        if sum == k:
            flag = 1
            break
        elif sum > k:
            j -= 1
        elif sum < k:
            i += 1
    if flag == 1:
        print(i,j)
    else:
        print("no answer")
    t -= 1

