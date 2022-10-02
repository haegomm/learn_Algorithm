import sys
sys.stdin = open('input.txt', encoding='utf-8')

def dfs(s):
    visited[s] = True
    global g

    for next_v in graph[s]:
        if not visited[next_v]:
                dfs(next_v)

t = int(input())

for tc in range(1, t+1):
    # 노드 v, 간선 e
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    visited = [False]*(v+1)

    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    # 확인 노드 s, 도착 노드 g
    s, g = map(int, input().split())

    dfs(s)

    if visited[g] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')