def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)


edges = list(map(int, input().split()))
n = max(edges)
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 인접 리스트 만들기
for i in range(0, len(edges), 2):
    v1, v2 = edges[i], edges[i+1]
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(1)