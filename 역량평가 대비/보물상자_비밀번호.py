# import sys
#
# sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    password = input()
    open = []
    turn = n // 4

    for _ in range(turn):
        for i in range(0, n - turn + 1, turn):
            open.append(int(password[i:i + turn], 16))

        password = password[-1] + password[:n-1]

    print(open)
    result = sorted(set(open), reverse=True)
    print(result)

print(f'#{t} {result[k-1]}')



