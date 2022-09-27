import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    station = list(map(int, input().split()))
    now_index = 1  # index 위치
    move = 1
    cnt = 0

    while now_index < station[0]:
        can_move = 0  # 이동한 최대거리
        for i in range(1, station[now_index] + 1):
            if now_index + i >= station[0]:
                break
            if station[now_index + i] + now_index + i >= can_move:
                can_move = station[now_index + i] + now_index + i
            now_index += (can_move - now_index + i)  # 이동한 위치...인덱스로 보는 위치
        # move += can_move
        # if move >= station[0]:
        #     break
        cnt += 1

    print(f'#{t}', cnt)