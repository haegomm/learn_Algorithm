# kruskal

# prim
from heapq import heappop, heappush

def prim(start):
    visited = [False] * (n + 1)
    heap = [(0, start)]
    cost = 0

    while heap:
        min_dist, min_node = heappop(heap)
        if visited[min_node]:
            continue

        visited[min_node] = True
        cost += min_dist

        for next_node, w in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (w, next_node))
    return cost


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

print(prim(1))