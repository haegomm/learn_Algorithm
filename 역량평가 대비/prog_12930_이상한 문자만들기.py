def solution(s):
    # words = s.split()
    answer = ''

    # for word in words:
    for i in range(0, len(s), 2):
        s = s.replace(s[i], s[i].upper(), 1)

    return s

print(solution("try hello world"))