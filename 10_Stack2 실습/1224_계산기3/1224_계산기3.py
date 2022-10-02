import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    length = int(input())
    word = input()
    result = ''
    stack = []

    for token in word:
        if token in '*+()':
            if not stack or token == '(':
                stack.append(token)
            elif token == '*':
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(token)
            elif token == '+':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()

        else:
            result += token

    while stack:
        result += stack.pop()

    for char in result:
        if char not in '*+':
            stack.append(int(char))
        else:
            x = stack.pop()
            y = stack.pop()
            if char == '+':
                stack.append(y + x)
            elif char == '*':
                stack.append(y * x)

    print(f'{tc} {stack.pop()}')