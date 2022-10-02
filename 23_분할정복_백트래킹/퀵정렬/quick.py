def partition(l, r):
    pivot = a[l]  # 피봇 값을 제일 왼쪽 값으로 줌
    i, j = l, r
    while i <= j:                        # i와 j가 역전되지 않는 동안 반복
        while i <= j and a[i] <= pivot:  # pivot 보다 큰 값 찾기?
            i += 1
        while i <= j and a[j] >= pivot:  # pivot 보다 작은 값 찾기?
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
        a[l], a[j] = a[j], a[l]
        return j


def qsort(l, r):
    if l < r:
        s = partition(l, r)
        qsort(l, s-1)
        qsort(s+1, r)


t = int(input())

for tc in range(1, t+1):

    a = list(map(int, input().split()))
    n = len(a)
    qsort(0, n-1)
    print(a)