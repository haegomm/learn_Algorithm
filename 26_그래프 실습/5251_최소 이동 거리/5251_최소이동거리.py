import sys

sys.stdin = open('input.txt', encoding='utf-8')

def dijkstra(start):
    visited = [False] * (n + 1)
    visited[start] = True
    distance[start] = 0

    for e, w in graph[start]:
        distance[e] = w

    for _ in range(n - 1):
        min_dist = inf
        for i in range(1, n + 1):
            if not visited[i] and min_dist > distance[i]:
                min_node = i
                min_dist = distance[i]

        visited[min_node] = True

        for next_node, dist in graph[min_node]:
            new_dist = distance[min_node] + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    inf = 99999999
    distance = [inf] * (n+1)

    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

        dijkstra(0)