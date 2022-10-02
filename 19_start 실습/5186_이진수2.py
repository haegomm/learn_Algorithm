t = int(input())

for tc in range(1, t+1):
    number = input()
    k = number[2:]

    for i in k:
        j = format(int(i), 'b')
        print(j)