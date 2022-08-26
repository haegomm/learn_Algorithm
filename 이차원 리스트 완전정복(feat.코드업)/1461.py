n = int(input())
arr = [[0]*n for _ in range(n)]
k = 1

for i in range(n):
    for j in range(n-1, -1, -1):
        arr[i][j] = k
        k += 1

for line in arr:
    print(*line)
