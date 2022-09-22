# import sys
# sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())    # n 화물 m 트럭
    containers = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())))
    result = 0

    for _ in range(n):
        # if len(containers) == 0 or len(trucks) == 0:
        #     break
        if containers[-1] <= trucks[-1]:
            result += containers[-1]
            containers.remove(containers[-1])
            trucks.remove(trucks[-1])
        else:
            containers.remove(containers[-1])

    print(f"#{tc} {result}")