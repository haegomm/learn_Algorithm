# 특정 원소가 속한 집합 찾기 (루트 노드 찾기)
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])  # 경로 압축(Path compression)
                                               # 갱신하면서 return 내려온다.
    return parent[node]


n, m = map(int, input().split())  # 정점, 간선 개수
edges = []
for _ in range(m):
    s, e, w = map(int, input().split())  # 시작 정점, 도착 정점, 비용
    edges.append((w, s, e))  # 맨 앞의 값부터 정렬하기 때문에 w를 맨 앞으로 빼줌

edges.sort()  # (중요) 최소 비용의 간선부터 차례로 검사하기 위해 비용을 기준으로 오름차순 정렬

parent = list(range(n + 1))  # make_set. +1 은 컴퓨터는 0부터 시작하니깐
print(parent)
counts = 0  # MST의 간선 개수 (정점 - 1 개가 되면 종료를 하기 위함)
            # 더 이상 간선을 선택하지 않아도 되는 때를 판별
cost = 0  # MST의 가중치 총합(== 최소 비용)

for dist, x, y in edges:
    x_root, y_root = find_set(x), find_set(y)  # x와 y의 각각 대표값

    if x_root != y_root:  # 사이클이 아니면 == 서로소라면 == 다른 집합이라면
        parent[y_root] = x_root  # union
        cost += dist
        counts += 1  # 효율성을 위해서.
                     # 간선이 다 만들어지면 다른 간선들을 더 이상 안 봐도 되니깐 종료키면 됨.
                     # 그걸 위해서 count (백트래킹, 가지치기)

        if counts >= n - 1:  # 간선의 최대 개수는 정점 - 1 이므로 break
            break

print(cost)

"""
[입력]

7 11
1 2 32
1 3 31
1 6 60
1 7 51
2 3 21
3 5 46
3 7 25
4 5 34
4 6 18
5 6 40
5 7 51
"""