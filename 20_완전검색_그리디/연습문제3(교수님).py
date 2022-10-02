arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
for i in range(1, 1 << N):
    s = 0
    for j in range(N):
        if i & (1 << j):
            s += arr[j]

    if s == 0:
        for j in range(N):
            if i & (1 << j):
                print(arr[j], end=' ')
        print()
print(f'{1<<N}의 부분집합 중 ')


def f(i, N, s):
    if i == N:
        if s == 0 and sum(bit) != 0:  # sum(bit) != 0 공집합 제거
            for j in range(N):
                if bit[j]:
                    print(arr[j], end=' ')
            print()
    else:
        bit[0] = 0
        f(i + 1, N, s)
        bit[i] = 1
        f(i + 1, N, s + arr[i])


bit = [0] * N
f(0, N, 0)
