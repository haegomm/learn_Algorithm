import sys

sys.stdin = open('input.txt', encoding='utf-8')

for t in range(1, int(input()) + 1):
    k, n, m = map(int, input().split()) # k 최대 이동거리 n 종점 m 정류소 갯수
    m_list = list(map(int, input().split()))

    now = 0
    cnt = 0

    while now + k < n:
        for move in range(k, 0, -1):
            if (now + move) in m_list or now == n:
                now += move
                cnt += 1
                break
        else:
            cnt = 0
            break

    print(f'#{t} {cnt}')