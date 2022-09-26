import sys

sys.stdin = open('input.txt', encoding='utf-8')

# for t in range(1, int(input()) + 1):
#     n, q = map(int, input().split())
#     box = [0] * (n + 1)
#
#     for i in range(1, q+1):
#         l, r = map(int, input().split())
#
#         for k in range(l, r+1):
#             box[k] = i
#
#     print(f'#{t}', *box[1:])

for case in range(1, 1 + int(input())):
    N, Q = map(int, input().split())  # N = 상자길이, Q = 횟수
    arr = [0] * N  # 상자
    for _ in range(Q):
        L, R = map(int, input().split())
        for i in range(L-1, R):
            arr[i] = L
    print(f'#{case}', *arr)