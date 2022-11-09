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
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < k and 0 <= ny < k:
                        check.append((nx, ny))

    # 확인할 얼음의 인접 얼음들 확인
    for x, y in check:
        cnt = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
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




n, q = map(int, input().split())
k = 2**n
arr = [list(map(int, input().split())) for _ in range(k)]
stages = list(map(int, input().split()))

for stage in stages:
    trun(stage)
