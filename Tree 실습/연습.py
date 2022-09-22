# a = map(int, ["1", "2"])
# print(a)
# for i in a:
#     print(i)

# b = list(a)
# print(b)

# a = [i for i in range(10)]
# print(a)

# a = (i for i in range(10))
# print(a)


# 동적계획법(dp)
matrix = [list(map(int, input().split()))]
memo = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 1. 원래 리스트의 값을 더한다.
        memo[i][j] += matrix[i][j]

        if i == 0 and j == 0:  # 0,0 일 때는 위랑 왼쪽이 없으니깐
            continue

        # 2. 위, 왼쪽을 더해서 최소합으로 갱신
        if i == 0:  # 위가 없음
            memo[i][j] += memo[i][j - 1]  # 왼쪽 더해주기
        elif j == 0:
            memo[i][j] += memo[i - 1][j]
        else:  # 나머지 부분
            memo[i][j] += min(memo[i - 1][j], memo[i][j - 1])

print('f{tc} {memo[n-1][n-1]}')
