t = int(input())

for tc in range(1, t+1):
    numbers = input()

    for i in range(0, len(numbers), 7):
        num = int(numbers[i:i+7], 2)
        print(num, end=' ')

