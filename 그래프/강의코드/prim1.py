def prim1(r, V):
    mst = [0] * (v+1)  # mst 포함여부
    key = [10000] * (v+1)  # 가중치의 최대값 이상으로 초기화. key[v]는 v가 mst에 속한 정점과 연결 될
    key[r] = 0  # 시작정점의 key
    for _ in range(v):  # v + 1개의 정점 중 v 개를 선택
        # mst에 포함되지 않은 정점 중(mst[u] == 0), key가 최소인 u 찾기
        u = 0
        minv = 10000
        for i in range(v+1):
            if mst[i] == 0 and key[i] < minv:
                u = i
                minv = key[i]
        mst[u] = 1  # 정점 u를 mst에 추가
        # u에 인접인 v에 대해, mst에 포함되지 않은 정점이면
        for v in range(v+1):
            if mst[v] == 0 and adjm[u][v] > 0:
                key[v] = min(key[v], adjm[u][v])  # u를 통해 mst에 포함되는 비용과 기존
    return sum(key)  # mst 가중치의 합


V, e = map(int, input().split())
adjm = [[0]*(V+1) for _ in range(V+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    adjm[u][v] = w
    adjm[v][u] = w  # 가중치가 있는 무방향 그래프

prim1(0, V)