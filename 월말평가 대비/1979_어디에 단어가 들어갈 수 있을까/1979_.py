import sys

sys.stdin = open('input.txt', encoding='utf-8')

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr_row = [input().replace(" ", "") for _ in range(n)]
    arr_col = list(map(''.join, zip(*arr_row)))
    cnt = 0

    for arr in arr_row, arr_col:
        for line in arr:
            # print(line)
            real = list(line.split('0'))
            # print(real)
            # real = real.pop('')  # TypeError: 'str' object cannot be interpreted as an integer
            # real.remove('')
            for check in real:
                if check == ('1' * k):
                    cnt += 1

    print(f'#{t}', cnt)