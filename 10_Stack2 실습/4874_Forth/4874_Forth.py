import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    word = input().split()
    result = ''
    stack = []

    for char in word:

        if char not in '*/+-.':
            stack.append(int(char))
        # 입력값의 맨 마지막에 .이 오니깐 .이 나오면 문장이 끝났다는 얘기!
        # 그래서 .이 나오면 이제 stack에 있는 값의 예외들을 확인하면서 error 또는 결과 값을 출력~!
        elif char == '.':
            # stack에 1개 이상의 값이 있으면 연산 실패로 error 출력
            if len(stack) != 1:
                print(f'#{tc} error')
            # stack에 남아있는 값이 1개라면 그걸 출력한다.
            else:
                print(f'#{tc} {stack.pop()}')
        else:
            # 연산 중간에 사용할 피연산자가 다 떨어진 경우도 error 출력
            if len(stack) < 2:
                print(f'#{tc} error')
                break
            else:
                x = stack.pop()
                y = stack.pop()
                if char == '*':
                    stack.append(y * x)
                elif char == '/':
                    stack.append(y // x)
                elif char == '+':
                    stack.append(y + x)
                elif char == '-':
                    stack.append(y - x)
