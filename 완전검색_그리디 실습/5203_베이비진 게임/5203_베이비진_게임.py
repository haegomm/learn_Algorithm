import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    card = list(map(int, input().split()))
    tri_1 = [0] * 12
    run_1 = ''
    tri_2 = [0] * 12
    run_2 = ''
    game = 0
    result = 0

    for i in card:
        if result != 0:
            break
        if game % 2 == 0:  # 짝수 - 플레이어1
            if tri_1[i] == 0:
                tri_1[i] = 1
            run_1 += str(i)

        else:  # 홀수 - 플레이어2
            if tri_2[i] == 0:
                tri_2[i] = 1
            run_2 += str(i)

        # run_1 = sorted(run_1)
        # run_2 = sorted(run_2)
        game += 1

        if game >= 5:
            for k in range(10):
                if tri_1[k] + tri_1[k+1] + tri_1[k+2] == 3 or run_1.count(str(k)) == 3:
                    result = 1
                    break
                elif tri_2[k] + tri_2[k+1] + tri_2[k+2] == 3 or run_2.count(str(k)) == 3:
                    result = 2
                    break

    print(f'#{tc}', result)


