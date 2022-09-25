import sys

sys.stdin = open('input.txt', encoding='utf-8')

# for t in range(1, int(input()) + 1):
#     n = int(input())
#     move = []
#     stations = []
#     for _ in range(n):
#         move += list(map(int, input().split()))
#     p = int(input())
#     result = [0] * p
#
#     for _ in range(p):
#         stations.append(int(input()))
#
#     for i in range(0, len(move), 2):
#         for j in stations:
#             if move[i] <= j <= move[i+1]:
#                 idx = stations.index(j)
#                 result[idx] += 1
#
#     print(f'#{t}', *result)

for t in range(1, int(input()) + 1):
    n = int(input())
    stations = [0] * 5001
    result = []

    for _ in range(n):
        a, b = map(int, input().split())

        for i in range(a, b+1):
            stations[i] += 1

    p = int(input())

    for _ in range(p):
        j = int(input())
        result.append(stations[j])

    print(f'#{t}', *result)