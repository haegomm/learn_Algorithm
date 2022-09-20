t = int(input())

for tc in range(1, t+1):
    numbers = input()
    arr = ''

    for i in numbers:
        binary = format(int(i, 16), 'b')
        print(binary)
        binary = '0' * (4 - len(binary)) + binary
        arr += binary
        print(binary)

    for i in range(0, len(arr), 7):
        num = int(arr[i:i+7], 2)
        print(num, end=' ')