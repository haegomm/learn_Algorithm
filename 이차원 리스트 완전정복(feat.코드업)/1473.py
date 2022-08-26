n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
k = 1

for row in range(n):
    for col in range(m):
        if not row % 2:
            arr[n-1-row][col] = k
        else:
            arr[n-1-row][m-1-col] = k
        k += 1

for line in arr:
    print(*line)