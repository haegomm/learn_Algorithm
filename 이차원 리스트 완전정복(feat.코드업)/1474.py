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


# for row in range(m-1, -1, -1):
#     for col in range(n):
#         if not row % 2:
#             arr[col][row] = k
#         else:
#             arr[n-1-col][row] = k
#         k += 1

for line in arr:
    print(*line)
