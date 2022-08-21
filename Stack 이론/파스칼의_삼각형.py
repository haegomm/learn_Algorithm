t = int(input())

for tc in range(1,t+1):
    n = int(input())
    print(f'#{tc}')


    in_triangle = [1]

    for i in range(1, n+1):
        triangle = []
        print(*in_triangle)
        in_triangle = [0] + in_triangle + [0]
        for j in range(i+1):
            triangle.append(in_triangle[j] + in_triangle[j+1])
        in_triangle = triangle

# for case in range(1, int(input()) + 1):
#     n = int(input())
#     print(f'#{case}')
#
#     li = []
#     li_0 = [1]
#
#     for i in range(1, n + 1):
#         print(*li_0)
#         li_0 = [0] + li_0 + [0]
#         li = [(li_0[j] + li_0[j+1]) for j in range(i+1)]
#         li_0 = li