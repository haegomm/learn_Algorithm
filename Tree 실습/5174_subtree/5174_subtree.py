import sys
sys.stdin = open('input.txt')


def find_child(n):
    if n == 0:
        return 0
    else:
        l = find_child(tree[n][0])
        r = find_child(tree[n][1])
        return l + r + 1


t = int(input())

for tc in range(1, t + 1):
    e, s = map(int, input().split())
    tree = [[0] * 3 for _ in range(e + 2)]
    edges = list(map(int, input().split()))

    # 이진트리 구현
    for i in range(0, len(edges), 2):
        parent, child = edges[i], edges[i + 1]

        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child

        tree[child][2] = parent

    print(f'{tc}', find_child(s))
