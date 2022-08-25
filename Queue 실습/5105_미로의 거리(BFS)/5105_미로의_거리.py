import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    global maze_success
    visited[x][y] = 1
    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] == 0:  # != 1
                if maze[i][j] == 2:  # 도착지점에 도착하면
                    maze_success = True
                    return visited[x][y]
                visited[nx][ny] = visited[x][y] + 1  # 이 부분 어려웠음.
                queue.append(nx, ny)



# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

for tc in range(1, t+1):

    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]  # 미로
    visited = [[0] * n for _ in range(n)]
    maze_success = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and maze[i][j] == 3:  # 출발 3 도착 2
                                                       # 만약에 방문하지 않았고 출발 지점이면 dfs를 시작한다.
                bfs(i, j)


    print(f'#{tc}', visited[x][y])