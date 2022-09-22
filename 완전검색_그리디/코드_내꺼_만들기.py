t = int(input())

for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    memo = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            memo[i][j] = board[i][j]

            if i == 0 and j == 0:
                continue

            if i == 0:
                memo[i][j] += memo[i][j-1]
            elif j == 0:
                memo[i][j] += memo[i-1][j]
            else:
                memo[i][j] += min(memo[i][j-1], memo[i-1][j])

    print(f'#{tc}', memo[n-1][n-1])