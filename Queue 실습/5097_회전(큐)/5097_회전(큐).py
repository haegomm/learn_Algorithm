import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())  # 숫자 갯수 n, 작업 횟수 m
    queue = list(map(int, input().split()))

    for _ in range(m):  # 작업 횟수 만큼 반복
        queue.append(queue.pop(0))  # pop한 걸 마지막으로 보내기

    print(f'#{tc} {queue.pop(0)}')
