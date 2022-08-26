n = int(input())
arr = [[0]*n for _ in range(n)]
k = 1

for row in range(n):
    if row % 2 == 0:
        for col in range(n):
            arr[row][col] = k
            k += 1
    else:
        for col in range(n-1, -1, -1):
            arr[row][col] = k
            k += 1


for line in arr:
    print(*line)