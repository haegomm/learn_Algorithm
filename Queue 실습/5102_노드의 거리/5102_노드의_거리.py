import sys
sys.stdin = open('input.txt')

def bfs(s, g):
    queue = [s]

    while queue:
        queue.pop(0)
        for join_v in graph[s]:
            if graph[join_v] == g:
                return
            queue.append(join_v)
            cnt
    return 0

t = int(input())

for tc in range(1, t + 1):

    # 노드 개수 v, 간선 정보 e개
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)] # 정점이 1부터 시작이라 v+1
    queue = []

    # 인접 리스트 만들어주기
    for i in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)  # 방향성이 없는 간선들이기 때문에 양쪽으로 정보 넣어주기.

    s, g = map(int, input().split())

    bfs(s, g)

print(f'#{tc}', bfs(s, g))
