def prim2(r, V):
    mst = [0]*(V+1)  # mst 포함여부
    mst[r] = 1  # 시작정점 표시
    s = 0  # mst 간선의 가중치 합
    for _ in range(V):
        u = 0
        minv = 10000
        for i in range(V+1):  # mst에 포함된 정점i와 인접한 정점j 중 mst에 포함
            if mst[i] == 1:
                for j in range(V+1):
                    if adjm[i][j] > 0 and mst[j] == 0 and minv > adjm[i][j]:
                        u = j
                        minv = adjm[i][j]
        s += minv
        mst[u] = 1
    return s


V, e = map(int, input().split())
adjm = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    adjm[u][v] = w
    adjm[v][u] = w  # 가중치가 있는 무방향 그래프

prim2(0, V)