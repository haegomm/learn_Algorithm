import sys

sys.stdin = open('input.txt')


# def go_s(line, i):
#     global result
#
#     for sg in range(i, n):
#         if line[sg] == 1:
#             break
#         elif line[sg] == 2:
#             result += 1
#             break
#
#
# def go_n(line, i):
#     global result
#
#     for ng in range(i, -1, -1):
#         if line[ng] == 2:
#             break
#         elif line[ng] == 1:
#             result += 1
#             break
#
#
# for t in range(1, 11):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     arr = list(map(list, zip(*arr)))
#     result = 0
#     # print(arr)
#
#     for line in arr:
#         for i in range(100):
#             if line[i] == 1:
#                 go_s(line, i+1)
#             elif line[i] == 2:
#                 go_n(line, i-1)
#     print(line)
#
#     print(f'#{t} {result}')


for t in range(1, 11):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    arr = list(map(''.join, zip(*arr)))
    print(arr)

    for line in arr:
        line = ' '.join(line.split('0')).split()

        print(line)