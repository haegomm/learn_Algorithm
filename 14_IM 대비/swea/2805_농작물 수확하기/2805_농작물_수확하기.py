import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    mf = n // 2
    harv = cnt = 0
    breaker = False

    for _ in range(n):
        farm = list(map(int, input()))
        harv += sum(farm[mf - cnt : mf + cnt + 1])
        if cnt == mf:
            breaker = True
        if breaker:
            cnt -= 1
        else:
            cnt += 1

    print(f'#{tc} {harv}')


    # n = int(input())
    # farm = [list(map(int, input())) for _ in range(n)]
    #
    # middle_farm = n // 2
    # harvest = 0
    # harv_cnt = 0
    # breaker = True
    #
    # for line== in farm:
    #     harvest += sum(line[(middle_farm - harv_cnt) : (middle_farm + harv_cnt + 1)])
    #     if harv_cnt == middle_farm:
    #         breaker = False
    #     if breaker:
    #         harv_cnt += 1
    #     else:
    #         harv_cnt -= 1
    #
    # print(f'#{tc} {harvest}')


