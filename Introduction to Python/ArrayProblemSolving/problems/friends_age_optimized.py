n = int(input())
arr = [int(i) for i in input().split()]
ans = 0
freq = {}
for i in arr:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

for i in range(1,121):
    for j in range(1,121):
        if (i in freq) and (j in freq):
            if (j <= 0.5 * i + 7) or (j > 100 and i <100) or (j > i):
                continue
            ans += freq[i] * freq[j]
            if (i == j):
                ans -= freq[i]

print(ans)