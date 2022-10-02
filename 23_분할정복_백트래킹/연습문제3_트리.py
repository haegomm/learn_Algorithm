def preorder(node):
    if node != 0:
        print(node, end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print(node, end=' ')
        inorder(tree[node][1])


def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end=' ')


v, e = map(int, input().split())
edge = list(map(int, input().split()))
tree = [[0] * 3 for _ in range(v+1)]

# 트리 만들기
for i in range(0, e * 2, 2):
    parent, child = edge[i], edge[i+1]

    if tree[parent][0] == 0:
        tree[parent][0] = child
    else:
        tree[parent][1] = child

    tree[child][2] = parent

preorder(1)
print()
inorder(1)
print()
postorder(1)

