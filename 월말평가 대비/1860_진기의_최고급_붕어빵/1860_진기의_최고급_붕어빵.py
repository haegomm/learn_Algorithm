import sys

sys.stdin = open('input.txt', encoding='utf-8')

for t in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    guest = sorted(list(map(int, input().split())))
    bung = 0
    result = 'Possible'

    for time in range(1, 11112):
        if time % m == 0:
            bung += k

        if time in guest:
            if bung <= 0:
                result = 'Impossible'
                break
            else:
                bung -= 1

    print(f'#{t} {result}')
