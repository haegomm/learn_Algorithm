import sys
sys.stdin = open('input.txt')

# t = int(input())
#
# for tc in range(1, t+1):
#
#     sudoku = [list(map(int, input().split())) for _ in range(9)]
#     sudoku_col = list(map(list, zip(*sudoku)))
#     check = list(range(1, 10))
#     result = 1
#     breaker = False
#
#     # 3x3 검사
#     for r in range(0, 7, 3):
#         if breaker:
#             break
#         for c in range(0, 7, 3):
#             box = []
#             for i in range(c, c + 3):
#                 for j in range(r, r + 3):
#                     box.append(sudoku[i][j])
#             box.sort()
#             if box == check:
#                 continue
#             else:
#                 result = 0
#                 breaker = True
#                 break
#
#     # 행 검사
#     for row in sudoku:
#         row.sort()
#         if row == check:
#             continue
#         else:
#             result = 0
#             break
#
#     # 열 검사
#     for col in sudoku_col:
#         col.sort()
#         if col == check:
#             continue
#         else:
#             result = 0
#             break
#
#     print(f'#{tc} {result}')

# 검사 함수 (집합 자료형 사용)
def chk(arr):
    if len(set(arr)) == 9:
        return 1
    return 0


for t in range(1, int(input()) + 1):
    # 스도쿠 입력 받기
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    # 행 검사하기
    sudoku_chk = 0 if 0 in set(map(chk, sudoku)) else 1
    # 행 에러
    if not sudoku_chk:
        print(f'#{t} {0}')
        continue
    # 열 검사
    reverse_chk = 0 if 0 in set(map(chk, zip(*sudoku))) else 1
    # 열 에러
    if not reverse_chk:
        print(f'#{t} {0}')
        continue
    # 3x3 박스 만들기
    box = []
    for row in range(0, 7, 3):
        for col in range(0, 7, 3):
            box.append(
                sudoku[row][col : col + 3]
                + sudoku[row + 1][col : col + 3]
                + sudoku[row + 2][col : col + 3]
            )
    # 박스 검사
    box_chk = 0 if 0 in set(map(chk, box)) else 1
    # 박스 에러
    if not box_chk:
        print(f'#{t} {0}')
        continue
    # 이상 없음
    print(f'#{t} {1}')