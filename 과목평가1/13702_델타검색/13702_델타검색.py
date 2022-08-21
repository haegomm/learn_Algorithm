import sys
sys.stdin = open('1in.txt', encoding='utf-8')


def get_abs(number):
    if number >= 0:
        return number
    else:
        return -number


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for tc in range(1, 11):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    total = 0

    for x in range(n):
        for y in range(n):
            temp = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    temp += get_abs(arr[nx][ny] - arr[x][y])

            total += temp

    print(f'#{tc} {total}')