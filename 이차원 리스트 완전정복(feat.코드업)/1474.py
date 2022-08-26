n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
k = 1

for col in range(m):
    for row in range(n):
        if not col % 2:
            arr[n-1-row][m-1-col] = k
        else:
            arr[row][m-1-col] = k
        k += 1

for line in arr:
    print(*line)
