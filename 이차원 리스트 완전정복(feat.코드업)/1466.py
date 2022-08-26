n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
k = 1

for col in range(m-1, -1, -1):
    for row in range(n-1, -1, -1):
        arr[row][col] = k
        k += 1

for line in arr:
    print(*line)