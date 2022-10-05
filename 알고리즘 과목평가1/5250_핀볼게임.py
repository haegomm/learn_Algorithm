import sys

sys.stdin = open('input.txt', encoding='utf-8')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
wh = {6, 7, 8, 9, 10}


def pinball(x, y):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        score = 0

        while 0 <= nx < n and 0 <= ny < n and board[nx][ny] != -1 and [nx][ny] != [x][y]:
            if nx == 0 or ny == 0 or nx == (n - 1) or ny == (n - 1) or board[nx][ny] == 5:
                score = (score * 2) - 1
                break

            elif board[nx][ny] in wh:
                for i in range(n):
                    for j in range(n):
                        if board[i][j] == board[nx][ny] and [i][j] != [nx][ny]:
                            nx = i
                            ny = j

            elif board[nx][ny] == 1:
                if d == 1:
                    d = 3
                elif d == 2:
                    d = 0
                elif d == 0:
                    d = 1
                elif d == 3:
                    d = 2
                score += 1

            elif board[nx][ny] == 2:
                if d == 0:
                    d = 3
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 2
                elif d == 1:
                    d = 0
                score += 1

            elif board[nx][ny] == 3:
                if d == 3:
                    d = 1
                elif d == 0:
                    d = 2
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                score += 1

            elif board[nx][ny] == 4:
                if d == 3:
                    d = 0
                elif d == 1:
                    d = 2
                elif d == 0:
                    d = 1
                elif d == 2:
                    d = 3
                score += 1

            nx += dx[d]
            ny += dy[d]


for t in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    scores = []

    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                scores += [pinball(i, j)]