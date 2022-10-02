from itertools import combinations
# import sys
# sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, top = map(int, input().split())
    arr = list(map(int, input().split()))
    subsets = []
    s = []
    # m = 1000000000

    # 부분집합 만들기
    for i in range(len(arr) + 1):
        subsets = list(combinations(arr, i))
        for i in subsets:
            check = sum(i)
            if check >= top:
                s.append(check)
    print(s)
    print(subsets)

    # for num in arr:
    #     size = len(subsets)
    #     for y in range(size):
    #         subsets.append(subsets[y]+[num])
    #         if sum(subsets[-1]) >= top:
    #             sum_list.append(sum(subsets[-1]))



    print(f'#{tc}', min(s) - top)