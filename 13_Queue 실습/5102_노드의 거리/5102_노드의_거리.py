import sys
sys.stdin = open('input.txt')


def bfs(s, g):
    queue = [s]

    while queue:
        now = queue.pop(0)  # 현재 노드를 pop한다
        for next_v in graph[now]:  # 현재 노드와 연결된 노드의 정보를 가져온다.
            if next_v == g:  # 만약 다음 노드가 도착지점이면
                visited[now] += 1  # 간선을 지나 도착하니 +1을 해주고
                return visited[now]  # 도착지점까지 몇개의 노드를 지나왔는지에 대한 값을 리턴한다.
            if not visited[next_v]:  # 이걸 안해주면 같은 곳만 맴돌게 될 수도 있다.
                                     # 맴돌지 않게 하기 위해 방문한데는 가지말자~!
                visited[next_v] = visited[now] + 1  # 지나온 노드들을 저장해야하니깐 now에서 +1 해주기!
                queue.append(next_v)  # 다음 노드에서 또 인접한 곳으로 가야하니 next_v노드를 인큐!

    return 0


t = int(input())

for tc in range(1, t + 1):

    # 노드 개수 v, 간선 정보 e개
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]  # 정점이 1부터 시작이라 v+1
    visited = [0] * (v+1) # 지나온 노드 갯수를 셀거라서 false가 아닌 0으로 채워진 리스트를 만든다!

    # 인접 리스트 만들어주기
    for i in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)  # 방향성이 없는 간선들이기 때문에 양쪽으로 정보 넣어주기.

    s, g = map(int, input().split())

    distance = bfs(s, g)  # 도착지점 가보자고~

    print(f'#{tc} {distance}')
