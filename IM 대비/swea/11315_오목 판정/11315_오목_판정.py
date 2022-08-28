import sys
sys.stdin = open('input.txt')

def gobang(i, j):
    global result
    gobang_cnt = 1  # 오목을 찾아서 들어온거니깐 1로 시작
    direction = 0
    start_i, start_j = i, j

    while True:
        ni = i + dx[direction]
        nj = j + dy[direction]
        if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 'o':
            i = ni  # 이동
            j = nj
            gobang_cnt += 1
            if gobang_cnt == 5:  # 연속된 오목 찾으면 반복문 탈출~
                result = 'YES'
                break
        else:
            direction += 1  # 범위 밖이고 오목이 없다면 방향을 바꿔서 탐색 시작
            if direction == 4:  # 가로 세로 대각선 다 검색했는데도 없으면 반복문 탈출
                break
            i = start_i  # i j 값 시작점으로 돌리기
            j = start_j
            gobang_cnt = 1


# 좌 하 ⬊ ⬋
dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]

t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    board = list(input() for _ in range(n))
    result = 'NO'

    for i in range(n):
        if result == 'YES':
            break
        for j in range(n):
            if board[i][j] == 'o':
                gobang(i, j)

    print(f'#{tc} {result}')

# while breaker:
    #     # 가로검사
    #     for col in range(n):
    #         if gobang_cnt == 5:
    #             result = 'YES'
    #             return result
    #         elif board[i][col] == '.':
    #             breaker = False
    #             break
    #         else:
    #             gobang_cnt += 1
    #
    #     # 세로검사
    #     for row in range(n):
    #         if gobang_cnt == 5:
    #             result = 'YES'
    #             return result
    #         elif board[row][j] == '.':
    #             breaker = False
    #             break
    #         else:
    #             gobang_cnt += 1
    #
    #     # 대각선 ⬊ 검사
    #     for _ in range(n):
    #         if gobang_cnt == 5:
    #             result = 'YES'
    #             return result
    #         i += 1
    #         j += 1
    #         if board[i][j] == 'o' and 0 <= i < n and 0 <= j < n:
    #             gobang_cnt += 1
    #         else:
    #             breaker = False
    #             break
    #
    #     # 대각선 ⬋ 검사
    #     for _ in range(n):
    #         if gobang_cnt == 5:
    #             result = 'YES'
    #             return result
    #         i += 1
    #         j -= 1
    #         if board[i][j] == 'o' and 0 <= i < n and 0 <= j < n:
    #             gobang_cnt += 1
    #         else:
    #             breaker = False
    #             break