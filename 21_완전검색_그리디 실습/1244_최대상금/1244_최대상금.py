import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    arr, cnt = input().split()

    arr = list(arr)
    new = sorted(arr, reverse=True)
    cnt = int(cnt)
    idx = 0
    max_idx = 0
    i = arr.index(str(new[idx]))

    while cnt:
        if arr != ''.join(new):
            if i != max_idx:
                arr[0], arr[i] = arr[i], arr[0]
                idx += 1  # idx, max_idx 범위 주기
                max_idx += 1
                cnt -= 1
            else:
                idx += 1
        else:
            arr[-2], arr[-1] = arr[-1], arr[-2]

    print(f'#{tc}', arr)