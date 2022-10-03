import sys
sys.stdin = open('input.txt')

t = int(input())

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]

dol = [0, 2, 1]
dol_cnt = [0, 2, 2]
for tc in range(1, t+1):
    n, m = map(int, input().split())
    board = [[0] * (n + 1) for _ in range(n+1)]
    board[n // 2][n // 2 + 1], board[n // 2 + 1][n // 2] = 1, 1  # 1 == 흑돌
    board[n//2][n//2], board[n//2+1][n//2+1] = 2, 2              # 2 == 백돌
    print(board)
    find = False
    b = 2
    w = 2

    for _ in range(m):
        s_col, s_row, d = map(int, input().split())

        e_row = s_row
        e_col = s_col
        f_row = s_row
        f_col = s_col

        # 돌을 놓자
        board[s_row][s_col] = d
        if d == 1:
            b += 1
        else:
            w += 1


        # 돌을 찾자
        k = 0
        while k <= 7:
            n_row = e_row + dx[k]
            n_col = e_col + dy[k]
            if 1 <= n_row <= n and 1 <= n_col <= n and board[n_row][n_col] == dol[d]:
                e_row = n_row
                e_col = n_col
                find = True

            elif 1 <= n_row <= n and 1 <= n_col <= n and board[n_row][n_col] == d and find:
                # 돌을 뒤집자
                while True:  # 이 동안 반복하고 싶어 그치만 이거말고 다르게 조건 걸어야할듯
                    f_row += dx[k]
                    f_col += dy[k]
                    print(f_row, f_col, e_row, e_col)
                    board[f_row][f_col] = d
                    if d == 1:
                        b += 1
                        w -= 1
                    else:
                        b -= 1
                        w += 1
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
        print(s_row, s_col, e_row, e_col)


    # 무슨 돌이 많을까~?
    print(f'#{tc} {b} {w}')



import sys
sys.stdin = open('input.txt')

t = int(input())

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]

dol = [0, 2, 1]
dol_cnt = [0, 2, 2]
for tc in range(1, t+1):
    n, m = map(int, input().split())
    board = [[0] * (n + 1) for _ in range(n+1)]
    board[n // 2][n // 2 + 1], board[n // 2 + 1][n // 2] = 1, 1  # 1 == 흑돌
    board[n//2][n//2], board[n//2+1][n//2+1] = 2, 2              # 2 == 백돌
    find = False

    for _ in range(m):
        s_col, s_row, d = map(int, input().split())

        e_row = s_row
        e_col = s_col
        f_row = s_row
        f_col = s_col

        # 돌을 놓자
        board[s_row][s_col] = d
        dol_cnt[d] += 1


        # 돌을 찾자
        k = 0
        while k <= 7:
            n_row = e_row + dx[k]
            n_col = e_col + dy[k]
            if 0 == n_row == n+1 or 1 <= n_col <= n: # 0인 돌을 만났을 때도 방향 바꾸자~~~
                k += 1
                e_row, e_col = s_row, s_col
                find = False
            elif board[n_row][n_col] == dol[d]:
                e_row = n_row
                e_col = n_col
                find = True

            elif board[n_row][n_col] == d and find:
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

    # 무슨 돌이 많을까~?
    print(f'#{tc}', *dol_cnt[1:])









