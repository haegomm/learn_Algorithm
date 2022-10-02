import sys

sys.stdin = open('input.txt', encoding='utf-8')


def bfs(n, m):
    q = [1]
    visited = [0] * (n+1)
    visited[1] = 1
    cnt = 0
    while q:
        t = q.pop(0)
        cnt += 1
        if visited[t] <= 2:  # 상원이의 친구면
            for i in range(1, n+1):
                if adj[t][i] == 1 and visited[i] == 0:
                    q.append(i)
                    visited[i] = visited[t] + 1
    return cnt - 1


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    adj = -[[0] * (n + 1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1
    ans = bfs(n, m)
    print(f'#{tc}', ans)