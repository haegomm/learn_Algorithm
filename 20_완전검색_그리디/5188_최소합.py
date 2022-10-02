import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    memo = [[0] * n for _ in range(n)]

    for i in range(n):                          # memo 이차원배열과 board 이차원 배열을 탐색해보자
        for j in range(n):
            memo[i][j] += board[i][j]           # 일단 각 memo 위치에 알맞는 board의 위치 값을 더해준다.

            if i == 0 and j == 0:               # 0,0 일 때는 넘어간다.
                continue                        # 출발점이니깐 아무것도 더해주면 안되기 때문~!!

            if i == 0:
                memo[i][j] += memo[i][j-1]      # row 맨 윗줄인 경우 왼쪽 값만 더해주면 된다(오른쪽 이동이니깐 왼쪽값 더해주기)
            elif j == 0:
                memo[i][j] += memo[i-1][j]      # col 맨 왼쪽인 경우 윗쪽 값만 더해주면 된다(아래 이동이니깐 윗쪽값 더해주기)
            else:
                memo[i][j] += min(memo[i][j-1], memo[i-1][j])  # 나머지의 경우 오른쪽이나 아랫쪽 값 중 더 작은 값을 더해준다.
                                                               # 더해주는게 이동~!

    print(f'#{tc} {memo[n-1][n-1]}')