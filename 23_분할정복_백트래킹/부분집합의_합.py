def f1(i, k, t):  # t는 구하는 합
    global cnt
    cnt += 1
    if i == k:
        s = 0
        for j in range(10):
            if bit[j]:
                s += a[j]
        if s == t:
            for j in range(10):
                if bit[j]:
                    print(a[j], end=' ')
        else:
            bit[i] = 0
            f1(i+1, k, t)
            bit[i] = 1
            f1(i+1, k, t)


def f2(i, k, t, s):
    global cnt
    cnt += 1
    if i == k:
        if t == s:
            for j in range(10):
                if bit[j]:
                    print(a[j], end=' ')
                print()
    elif t <= s:  # 가지치기
        return
    else:
        bit[i] = 0
        f2(i+1, k, t, s)
        bit[i] = 1
        f2(i+1, k, t, s+a[i])
        return


def f3(i, k, t, s, rs):  # 가지치기 1개 더 추가
    global cnt
    cnt += 1
    if i == k:
        if t == s:
            for j in range(10):
                if bit[j]:
                    print(a[j], end=' ')
                print()
    elif t <= s:  # 가지치기
        return
    elif t > s + rs:  # 가지치기
        return
    else:
        bit[i] = 0
        f2(i+1, k, t, s, rs-a[i])
        bit[i] = 1
        f2(i+1, k, t, s+a[i], rs-a[i])
        return


a = [i for i in range(1, 11)]
bit = [0] * 10
cnt = 0
f1(0, 10, 10)
f2(0, 10, 10, 0)
f3(0, 10, 10, 0, sum(a))
print(cnt)