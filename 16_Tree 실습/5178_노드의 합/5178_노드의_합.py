import sys
sys.stdin = open('input.txt')


def post_order(k):
    if k <= n:
        l = post_order(k * 2)
        r = post_order(k * 2 + 1)
        return l + r + tree[k] # 마지막 리프값을 반환해주기 위해서 tree[k]도 더해줘야함. 마지막 리프 값에는 값이 담겨있다고 했기 때문에. 리프는 0이 아님!!!!!!!!!!!
    return 0 # 안해주면 none 담겨서 l = none 이렇게돼서 0을 리턴해줘야함.


t = int(input())

for tc in range(1, t + 1):
    n, m, p = map(int, input().split())
    tree = [0] * (n + 1)

    for _ in range(m):
        leaf, num = map(int, input().split())
        tree[leaf] = num

    print(f'#{tc}', post_order(p)) # p가 서브트리의 루트라서. 나머지 애들은 안봐도 됨. 그래서 바로 p 부르기~!~!~!