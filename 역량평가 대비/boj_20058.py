<<<<<<< HEAD
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
    global arr
    print(2)
    zero_friends = []

    # 0인 얼음을 먼저 찾기
    for i in range(k):
        for j in range(k):
            if not firestorm[i][j]:
=======
# 배열을 단계별로 회전시키기
def trun(s):
    new = [[0]*k for _ in range(k)]

    for i in range(0, k - s + 1, s):
        for j in range(0, k - s + 1, s):
            new[j][k-s-i] = arr[i][j]

    check_ice(new)

# 얼음 확인
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_ice(new):

    check = []

    # 0인 얼음 찾아서 확인할 얼음 리스트 만들기
    for i in range(k):
        for j in range(k):
            if new[i][j] == 0:
>>>>>>> 654183155016e75adb3533efd921f7300ae9b836
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < k and 0 <= ny < k:
<<<<<<< HEAD
                        zero_friends.append((nx, ny))

    for x, y in zero_friends:
=======
                        check.append((nx, ny))

    # 확인할 얼음의 인접 얼음들 확인
    for x, y in check:
>>>>>>> 654183155016e75adb3533efd921f7300ae9b836
        cnt = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
<<<<<<< HEAD
            if 0 <= nx < k and 0 <= ny < k and not firestorm[nx][ny]:
                # 0인 얼음이 있으면 +
                cnt += 1
                # 0인 얼음이 주변에 1개보다 많으면 -
                if cnt > 1:
                    firestorm[x][y] -= 1
                    break

    zero_friends.clear()


# 가장 큰 얼음덩어리 찾기
def dfs(x, y):
    global ice_size

    print(3)
    visited[x][y] = True
    ice_size += 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < k and 0 <= ny < k and not visited[nx][ny] and not arr[nx][ny]:
            dfs(nx, ny)
=======
            if 0 <= nx < k and 0 <= ny < k and new[nx][ny] == 0:
                cnt += 1
                if cnt > 1:
                    new[x][y] -= 1

    check.clear()

    # 남아있는 얼음의 합
    ice_sum = 0

    for line in new:
        ice_sum += sum(line)

    bigice(new)


def bigice():

    visited = [[False] * k for _ in range(k)]

    ice_size = []

    for i in range(k):
        for j in range(k):
            if not visited[i][j]:


>>>>>>> 654183155016e75adb3533efd921f7300ae9b836


n, q = map(int, input().split())
k = 2**n
arr = [list(map(int, input().split())) for _ in range(k)]
stages = list(map(int, input().split()))
<<<<<<< HEAD
visited = [[False] * k for _ in range(k)]
ice_sum = 0
big_ice = 0

for stage in stages:
    turn(2 ** stage)

for line in arr:
    ice_sum += sum(line)

for i in range(k):
    for j in range(k):
        if not visited[i][j] and arr[i][j]:
            ice_size = 0
            dfs(i, j)
            if big_ice < ice_size:
                big_ice = ice_size

print(ice_sum, big_ice, sep='\n')

=======

for stage in stages:
    trun(stage)
>>>>>>> 654183155016e75adb3533efd921f7300ae9b836
