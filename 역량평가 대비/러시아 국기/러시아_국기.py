import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    flag = [input() for _ in range(n)]
    result = 0
    print(flag)
    result += m - flag[0].count('W')
    result
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            flag[i].count()
