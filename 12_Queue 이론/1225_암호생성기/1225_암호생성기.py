import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())

    # 암호 리스트(queue)를 만든다.
    queue = list(map(int, input().split()))

    find_password = True
    # 암호 리스트(queue)에 0이 담길 때 까지 반복한다.
    while find_password:
        for minus_num in range(1, 6):
            password_num = (queue.pop(0) - minus_num)
            if password_num <= 0:  # 만약에 빼기를 한 숫자가 0보다 작거나 같다면
                password_num = 0  # 그 숫자를 0으로 유지하고
                queue.append(password_num)  # 암호 리스트(queue)의 맨 뒤에 넣는다.
                find_password = False  # while문 탈출~!
                break
            queue.append(password_num)  # 0보다 크다면 그냥 바로 큐 맨 뒤에 넣는다.

    print(f'#{tc}', *queue)