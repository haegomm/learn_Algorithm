from npr import N


def f(i, k):
    global minV
    if i == k:  # 인데스 i == 원소의 개수
        s = 0  # 모든 j행에서 p[j]열을 골랐을 때의 합
        for j in range(k):
            s += arr[i][p[i]]
        if minV > s:
            minV = s
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i + 1, k)
            p[i], p[j] = p[j], p[i]


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = [i for i in range(N)] * n  # p[i] i 행에서 선택한 열 번호
    minV = n * 10
    f(0, n)
    print(f'#{tc} {minV}')
