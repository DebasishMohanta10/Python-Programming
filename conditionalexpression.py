#if-else conditional expression
# output_value1 if condition else output_value2
num =20
output = "even" if num % 2 == 0 else "odd"
print(output)



arr1 =[5,10,12,18,19,17,25,27,67,98]
largest = arr1[0]
for i in arr1:
    if i > largest:
        largest = i
# largest = max(arr1)
#Assume secondlargest =0
secondlargest = 0

for i in arr1:
    if i < largest:
        if i > secondlargest:
            secondlargest = i
print(secondlargest)

str = "to do job is a simple task to survive"
dict1 = {}
for i in str.split():
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
print(dict1)



