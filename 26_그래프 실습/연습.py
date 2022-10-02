def prim(start):
    # MST 포함 여부 확인 리스트 만들어주기
    visited = [False] * (n + 1)

    # MST에 속한 정점과 연결된 간선 비용 리스트
    distance = [inf] * (n + 1)

    # 시작 비용은 무조건 0
    distance[start] = 0

    # MST 비용 총합(== 최소비용)
    cost = 0

    # 모든 정점을 잇기 위해 정점 갯수만큼 반복하면서 MST 생성
    for _ in range(n):
        # 최소 비용 초기화
        min_dist = inf

        # distance 다 확인하면서 가장 적은 비용으로 이동 할 수 있는 노드 찾기
        for i, dist in enumerate(distance):

            # MST가 아니고, 최소 비용이라면
            if not visited[i] and dist < min_dist:

                # 최소 비용 노드, 최소 비용으로 담기
                min_node = i
                min_dist = dist

        # MST에 넣고 비용 더해주기
        visited[min_node] = True
        cost += min_dist

        # min_node 기준 방문하지 않은 인접정점들의 최소 비용으로 비용리스트 갱신
        for next_node, dist in graph[min_node]:
            if not visited[next_node] and dist < distance[next_node]:
                distance[next_node] = dist

        return cost


# 정점, 간선
n, m = map(int, input().split())

# (노드 연결, 비용) 담을 리스트 만들어주기
graph = [[] for _ in range(n+1)]

# 임의의 큰 수
inf = 99999999

# 그래프에 연결, 비용 정보 담기
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

# MST 시작 - prim
print(prim(1))