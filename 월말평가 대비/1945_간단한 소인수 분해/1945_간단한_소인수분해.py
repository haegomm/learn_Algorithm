import sys

sys.stdin = open('input.txt', encoding='utf-8')

for t in range(1, int(input()) + 1):
    n = int(input())
    numbers = [2, 3, 5, 7, 11]
    result = []
    cnt = 0
    i = 0

    while i < 5:
        if n % numbers[i] == 0:
            n //= numbers[i]
            cnt += 1
        else:
            result.append(cnt)
            cnt = 0
            i += 1

    print(f'#{t}', *result)