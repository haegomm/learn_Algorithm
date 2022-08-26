import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    global maze_success
    visited[x][y] = 1  # 일단 시작점에 1을 주고 시작
    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)  # 출발~!
        for k in range(4):  # 델타 검색으로 이동 가능한 곳 탐색한다
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] != 1:
                if maze[i][j] == 3:  # 도착지점에 도착하면
                    maze_success = True
                    return visited[x][y]
                visited[nx][ny] = visited[x][y] + 1  # 이 부분 어려웠음.
                queue.append((nx, ny))

    return 0


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

for tc in range(1, t+1):

    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]  # 미로
    visited = [[0] * n for _ in range(n)]
    maze_success = False
    distnace = 0

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:  # 출발지점 찾아서 탐색 시작
                distnace = bfs(i, j)


    print(f'#{tc}', distnace)