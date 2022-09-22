n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
result = 0

for i in range(n - 1, -1, -1):
    result += k // coins[i]  # coins가 k보다 커도 몫이 0이니깐 더해줘도 상관없음
    k %= coins[i]  # k를 동전 사용한거 뺀 만큼 갱신해줘야함

print(result)
