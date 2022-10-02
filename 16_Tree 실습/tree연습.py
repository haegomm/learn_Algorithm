# def find_root(n):
#     for node in range(1, n+1):
#         if tree[node][2] == 0:
#             return node
#
# def preorder(node):
#     if node != 0:
#         print(node, end=' ')
#         preorder(tree[node][0])
#         preorder(tree[node][1])
#
# def inorder(node):
#     if node != 0:
#         inorder(tree[node][0])
#         print(node, end=' ')
#         inorder(tree[node][1])
#
# def postorder(node):
#     if node != 0:
#         postorder(tree[node][0])
#         postorder(tree[node][1])
#         print(node, end=' ')
#
# v = int(input())
# tree = [[0]*3 for _ in range(v+1)]
# edge = list(map(int, input().split()))
#
# # 이진 트리 구현
# for i in range(0, len(edge), 2):
#     parent, child = edge[i], edge[i+1]
#
#     if tree[parent][0] == 0:
#         tree[parent][0] = child
#     else:
#         tree[parent][1] = child
#
#     tree[child][2] = parent
#
#     root = find_root(v)


# 트리를 만들어보자
# 입력값 받고, 트리 틀 만들기
v = int(input())
tree = [[0]*3 for _ in range(v+1)]
edge = list(map(int, input().split()))


def find_root(n):
    for node in range(1, n+1):
        if tree[node][2] == 0:
            return node


# 이진트리 만들기
for i in range(0, len(edge), 2):
    parent, child = edge[i], edge[i+1]

    if tree[parent][0] == 0:
        tree[parent][0] = child

    else:
        tree[parent][1] = child

    tree[child][2] = parent

    root = find_root(v)
