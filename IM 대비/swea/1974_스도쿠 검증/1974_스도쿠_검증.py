import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku_col = list(map(list, zip(*sudoku)))
    check = list(range(1, 10))
    result = 1
    breaker = False

    # 3x3 검사
    for r in range(0, 7, 3):
        if breaker:
            break
        for c in range(0, 7, 3):
            box = []
            for i in range(c, c + 3):
                for j in range(r, r + 3):
                    box.append(sudoku[i][j])
            box.sort()
            if box == check:
                continue
            else:
                result = 0
                breaker = True
                break

    # 행 검사
    for row in sudoku:
        row.sort()
        if row == check:
            continue
        else:
            result = 0
            break

    # 열 검사
    for col in sudoku_col:
        col.sort()
        if col == check:
            continue
        else:
            result = 0
            break

    print(f'#{tc} {result}')
