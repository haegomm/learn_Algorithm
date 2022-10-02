t = int(input())

for tc in range(1, t+1):
    n, hexa = input().split()
    hexa = format(int(hexa, 16), 'b')
    hexa = '0' * (int(n)*4 - (len(hexa) % int(n))) + hexa

    print(f'#{tc}', hexa)