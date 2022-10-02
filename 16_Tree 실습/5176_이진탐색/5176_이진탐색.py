# import sys
# sys.stdin = open('input.txt')


def binary(k):
    global num
    if k <= n:
        binary(k * 2)
        tree[k] = num
        num += 1
        binary(k * 2 + 1)


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    tree = [0] * (n + 1)
    num = 1
    binary(1)

    print(f'#{tc}', tree[1], tree[n//2])