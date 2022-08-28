n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]


def get_abs(number):
    if number >= 0:
        return number
    else:
        return -number


black = 0
white = 0
middle = (n * m) // 2

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'B':
            black += 1
        else:
            white += 1

result_b = get_abs(middle - black)
result_w = get_abs(middle - white)

print(get_abs(result_b - result_w))