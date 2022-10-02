import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    station = list(map(int, input().split()))
    now = 1
    can = 0
    cnt = 0

    while now + station[now] <= station[0] - 1:
        mm = 0
        can = 0
        for can in range(1, station[now] + 1):
            if mm <= now + can + station[now + can]:
                mm = now + can + station[now + can]
                go = can
        now += go
        cnt += 1

    print(f'#{t}', cnt)