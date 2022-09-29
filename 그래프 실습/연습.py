def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


n, m = map(int, input().split())
edges = []

for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((w, s, e))

edges.sort()

parent = list(range(n+1))
counts = 0
costs = 0

for w, x, y in edges:
    x_root, y_root = find_set(x), find_set(y)

    if x_root != y_root:
        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root

        costs += w
        counts += 1

        if counts <= n - 1:
            break