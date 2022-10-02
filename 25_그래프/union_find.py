# 1. 반복문
# def find_set(node):
#     while node != parent[node]:
#         node = parent[node]
#     return node


# # 2. 재귀
# def find_set(node):
#     if node != parent[node]:
#         return find_set(parent[node])
#     return node


# # 3. 재귀 - 경로 압축(부모 노드를 대표값으로 만듦)
def find_set(node):
    if node != parent[node]:  # 나와 내 부모가 다를 때만 반복
        parent[node] = find_set(parent[node])
    return parent[node]


n, m = map(int, input().split())  # 정점, 간선(Union 횟수) 개수
parent = list(range(n + 1))  # make_set

for _ in range(m):
    x, y = map(int, input().split())
    x_root, y_root = find_set(x), find_set(y)  # Find

    # Union
    if x_root != y_root:  # 서로소 집합인 경우만 합집합 연산(루트가 다르면 합칠거야) == 다른 집합이라면
        if x_root < y_root:  # 없어도 되는데 있는 이유는 편의를 위해서. 작은 값에 붙이는게 보기 더 좋아서 적어주는 것.
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root

# 출력
for i in range(1, n + 1):
    print(find_set(i), end=' ')

print()
print(parent)

"""
[입력]

6 4
5 6
4 5
3 4
1 3
"""