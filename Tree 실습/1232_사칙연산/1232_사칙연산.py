import sys
sys.stdin = open('input.txt')


def inorder(k):




for tc in range(1, 11):
    n = int(input())
    tree = [0, 0, 0] * (n+1)

    for _ in range(n):
        info = list(input().split())
        idx = int(info[0])
        if len(info) == 4:
            tree[idx] = info[1]
        else:
            tree[idx] = info[1]

    inorder(1)

    print(tree[1])