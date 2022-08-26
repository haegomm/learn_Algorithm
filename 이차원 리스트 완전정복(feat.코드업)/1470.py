n = int(input())
arr = [[0] * n for _ in range(n)]
k = 1

for col in range(n):
    if col % 2 == 0:
        for row in range(n):
            arr[row][col] = k
            k += 1
    else:
        for row in range(n-1, -1, -1):
            arr[row][col] = k
            k += 1

for line in arr:
    print(*line)