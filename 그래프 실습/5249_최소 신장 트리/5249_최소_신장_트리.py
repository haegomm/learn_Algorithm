import sys

sys.stdin = open('input.txt')

def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])

    return parent[node]


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, w = map(int, input().split())
        edges.append((w, s, e))

    edges.sort()

    parent = list(range(n + 1))  # make_set
    counts = 0
    costs = 0

    for dist, x, y in edges:  # find_set
        x_root, y_root = find_set(x), find_set(y)

        if x_root != y_root:  # 서로소라면 == 다른 집합이라면 union~!
            if x_root < y_root:
                parent[y_root] = x_root
            else:
                parent[x_root] = y_root

            costs += dist
            counts += 1

            if counts >= n:
                break

    print(f'#{t} {costs}')