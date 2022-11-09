# 얼음 회전
def turn(s):
    print(1)
    firestorm = [[0] * k for _ in range(k)]

    # for i in range(0, k, s):
    #     for j in range(0, k, s):
    #         for x in range(i, i + s):
    #             for y in range(j, j + s):
    #                 firestorm[y][x + s - 1] = arr[x][y]

    for y in range(0, k, s):
        for x in range(0, k, s):
            for i in range(s):
                for j in range(s):
                    firestorm[y + j][x + s - i - 1] = arr[y + i][x + j]

    print(firestorm)
    checkice(firestorm)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 인접 얼음들 확인
def checkice(firestorm):

    zero_friends = []

    # 0인 얼음을 먼저 찾기
    for i in range(k):
        for j in range(k):
            if not firestorm[i][j]:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < k and 0 <= ny < k:
                        zero_friends.append((nx, ny))

    zero_friends.clear()

    for x, y in zero_friends:
        cnt = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < k and 0 <= ny < k and not firestorm[nx][ny]:
                cnt += 1
                if cnt > 1:
                    firestorm[x][y] -= 1
                    
    # 꼭짓점 모서리 얼음 녹이기
    # 배열 바꾸기


def dfs(x, y):
    global ice_size

    visited[x][y] = True
    ice_size += 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < k and 0 <= ny < k and not visited[nx][ny] and not arr[nx][ny]:
            dfs(nx, ny)

    big_ice.append(ice_size)


n, q = map(int, input().split())
k = 2**n
arr = [list(map(int, input().split())) for _ in range(k)]
stages = [list(map(int, input().split()))]
visited = [[False] * k for _ in range(k)]
ice_sum = 0
big_ice = 0

for stage in stages:
    turn(2**stage)

for line in arr:
    ice_sum += sum(line)

for i in range(k):
    for j in range(k):
        if not visited[i][j] and not arr[i][j]:
            ice_size = 0
            dfs(i,j)
            if big_ice < ice_size:
                big_ice = ice_size

print(ice_sum, big_ice, sep='\n')