# 2) 힙을 이용한 프림 알고리즘
# 우선순위 큐 : 우선순위가 높은게 먼저 나간다.
# 최소 힙 : 최솟값 pop 보장
# 최대 힙 : 최댓값 pop 보장
from heapq import heappush, heappop


def prim(start):
    visited = [False] * (n + 1)  # MST에 포함 여부 리스트
    distance = [INF] * (n + 1)  # distance[v] => 정점 v가 MST에 속한 정점과 연결된 간선의 비용
    distance[start] = 0
    heap = [(0, start)]  # 힙 선언 [(비용, 정점)]
    cost = 0  # MST의 가중치 총합(== 최소 비용)

    while heap:
        # 1. 가장 적은 비용으로 이동 가능한 정점 찾기(Greedy)
        min_dist, min_node = heappop(heap)  # 최소힙이므로 튜플의 첫 번째 원소를 기준으로 최소값 pop
        if visited[min_node]:
            continue  # 이미 MST에 포함된 정점이라면 무시

        # 2. 해당 정점을 MST에 포함하고 비용 총합을 더함
        visited[min_node] = True
        cost += min_dist

        # 3. 해당 정점과 인접한 정점에 대해 최소 비용 갱신
        for next_node, dist in graph[min_node]:
            if not visited[next_node] and dist < distance[next_node]:
                distance[next_node] = dist
                heappush(heap, (dist, next_node))

    return cost


n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[] for _ in range(n + 1)]
INF = 99999999  # 나올 수 없는 임의의 큰 수

for _ in range(m):
    s, e, w = map(int, input().split())  # 시작 정점, 도착 정점, 비용
    graph[s].append((e, w))
    graph[e].append((s, w))

print(prim(1))  # 1번 정점에서 시작