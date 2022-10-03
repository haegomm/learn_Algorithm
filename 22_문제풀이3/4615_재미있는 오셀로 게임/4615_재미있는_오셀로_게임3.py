#  솔루션 코드를 작성합니다.
import sys

sys.stdin = open('input.txt')

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]

def find_dol(r, c, d):

    # 돌을 찾자
    for k in range(8):
        n_row = r + dx[k]
        n_col = c + dy[k]

        if 1 <= n_row <= n and 1 <= n_col <= n and board[n_row][n_col] == dol[d]:
            e_row = n_row
            e_col = n_col
            find = True

        elif 1 <= n_row <= n and 1 <= n_col <= n and board[n_row][n_col] == d and find:

        # 돌을 뒤집자
        while True:  # 이 동안 반복하고 싶어 그치만 이거말고 다르게 조건 걸어야할듯
            f_row += dx[k]
            f_col += dy[k]

            board[f_row][f_col] = d
            dol_cnt[d] += 1
        dol_cnt[dol[d]] -= 1

        if f_row == e_row and f_col == e_col:
            k += 1
            e_row, e_col = s_row, s_col
            find = False
            f_row, f_col = s_row, s_col
            break
    else:
        k += 1
        e_row, e_col = s_row, s_col
        find = False


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [[0] * (n + 1) for _ in range(n + 1)]
    board[n // 2][n // 2 + 1], board[n // 2 + 1][n // 2] = 1, 1  # 1 == 흑돌
    board[n // 2][n // 2], board[n // 2 + 1][n // 2 + 1] = 2, 2  # 2 == 백돌
    dol = [0, 2, 1]
    dol_cnt = [0, 2, 2]
    find = False

    for _ in range(m):
        s_col, s_row, d = map(int, input().split())

        # 돌을 놓자
        board[s_row][s_col] = d
        dol_cnt[d] += 1

        find_dol(s_row, s_col, d)

print(f'#{t} {dol_cnt[1:]}')