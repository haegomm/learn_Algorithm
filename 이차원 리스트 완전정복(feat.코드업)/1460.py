n = int(input())
# arr = [[0]*n for _ in range(n)]
# k = 1
for i in range(1, n*n+1):
    if i % n == 0:
        print(i, sep='\n')
    else:
        print(i, end=' ')

# for i in range(n):
#     for j in range(n):
#         arr[i][j] = k
#         k += 1
#
# for line in arr:
#     print(*line)