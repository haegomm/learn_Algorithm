# import sys
#
# sys.stdin = open('input.txt')


def find_set(node):
    if node != group[node]:
        group[node] = find_set(group[node])
    return group[node]


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    apply = list(map(int, input().split()))

    group = list(range(n+1))

    for i in range(0, m * 2 - 1, 2):
        x_root, y_root = find_set(apply[i]), find_set(apply[i+1])

        if x_root != y_root:
            if x_root < y_root:
                group[y_root] = x_root
            else:
                group[x_root] = y_root

    print(group)
    for k in range(1, n + 1):
        group[k] = find_set(k)

    print(group)
    group = set(group)
    print(f'#{t}', len(group) - 1)