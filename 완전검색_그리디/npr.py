# 단순 순열 생성 방법
for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            for k in range(1, 4):
                if k != i and k != j:
                    print(i, j, k)


# 재귀 호출을 통한 순셩 생성 방법
def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i + 1, k)
            p[i], p[j] = p[j], p[i]


p = [1, 2, 3]
f(0, 3)

# npr3
def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:  # a[j]가 아직 사용되지 않았으면
                used[i] = 1  # a[j] 사용됨으로 표시
                p[i] = a[j]  # p[i]는 a[j]로 결정
                f(i + 1, k)  # p[i+1] 값을 결정하러 이동
                used[j] = 0  # a[j]를 다른 자리에서 쓸 수 있도록 허용


N = 3
a = [i for i in range(1, N + 1)]
used = [0] * N
f(1, N)

# npr3 에서 r개만 고르기
def f(i, k, r):
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:
                used[i] = 1
                p[i] = a[j]
                f(i + 1, k, r)
                used[j] = 0


N = 0
R = 3
a = [i for i in range(1, N + 1)]
used = [0] * N
p = [0] * N
f(0, N, 3)
