import sys

sys.stdin = open('input.txt', encoding='utf-8')


def binary_search(a, k):
    global cnt
    s = 0
    e = len(a) - 1
    flag = 0

    while s <= e:
        m = (s + e) // 2
        if k == a[m]:
            cnt += 1
            return

        elif k < a[m] and flag != 1: # 왼쪽 탐색
            e = m - 1
            flag = 1  # 나 왼쪽 들렸어~!

        elif k > a[m] and flag != 2: # 오른쪽 탐색
            s = m + 1
            flag = 2  # 나 오른쪽 들렸어~!
        else:
            return


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    a = sorted(list(map(int,input().split())))
    b = list(map(int, input().split()))
    cnt = 0

    for key in b:
        binary_search(a, key)

    print(f'#{t}', cnt)