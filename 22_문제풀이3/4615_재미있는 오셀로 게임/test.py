# for i in range(2, 2):
#     print(i)

arr = [1, 2, 3, 4]
n = len(arr)
temp = []
subset = []

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            temp.append(arr[j])
    subset.append(temp)
    temp = []
            # print(numbers[j], end= ' ')
print(subset)