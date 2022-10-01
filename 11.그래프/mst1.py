v, e = map(int, input().split())
adjm = [[0]*(v+1) for _ in range(v+1)]
adjl = [[] for _ in range(v+1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    adjm[u][v] = w
    adjm[v][u] = w
    adjl[u].append((v, w))
    adjl[v].append(((u, w)))

