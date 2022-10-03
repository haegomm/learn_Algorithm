import sys

sys.stdin = open('input.txt', encoding='utf-8')

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]


def find_dol(r, c, d):

    for k in range(8):  # 모든 방향 다 탐색
        # 찾자
        nr = r + dx[k]  # 일단 한칸 이동
        nc = c + dy[k]

        # r,c
        # B W W 0
        # B 0 0 0
        # B B B B
        # B W B B
        # B W W B
        while 0 < nr <= n and 0 < nc <= n and board[nr][nc] and board[nr][nc] != d:  # 이동한 곳이 범위 내인지, 돌이 있는지 확인
            nr += dx[k]                                                              # 있다면 다음 칸으로 이동
            nc += dy[k]                                                              # 반복

        # 뒤집자
        if 0 < nr <= n and 0 < nc <= n and board[nr][nc] == d:  # 마지막으로 찾은 위치의 돌이 같은 색이면 그 내에 있는 다른 색 돌들을 뒤집는다
            sr = r + dx[k]                                      # sr, sc 는 시작 위치
            sc = c + dy[k]
            while True:
                if sr == nr and sc == nc:  # 시작 위치가 마지막 위치가 된다면 반복문 탈출
                    break
                board[sr][sc] = d     # 돌을 뒤집고
                dol_cnt[d] += 1       # 같은 색 돌 갯수 +1
                dol_cnt[dol[d]] -= 1  # 뒤집힌 돌 갯수는 -1
                sr += dx[k]           # 다음 돌 뒤집으러~
                sc += dy[k]


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [[0] * (n + 1) for _ in range(n + 1)]
    board[n//2][n//2+1], board[n//2+1][n//2] = 1, 1  # 흑 == 1
    board[n//2][n//2], board[n//2+1][n//2+1] = 2, 2  # 백 == 2
    dol = [0, 2, 1]       # 뒤집을 돌
    dol_cnt = [0, 2, 2]   # 돌 갯수 세기

    for _ in range(m):
        col, row, d = map(int, input().split())

        # 일단 놓자
        board[row][col] = d
        dol_cnt[d] += 1

        find_dol(row, col, d)

    print(f'#{t}', *dol_cnt[1:])