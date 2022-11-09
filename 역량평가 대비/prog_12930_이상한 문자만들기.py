def solution(s):
    words = s.split(' ')
    answer = []

    for word in words:
        new_word = ''
        for i, values in enumerate(word):
            if i % 2 == 0:
                new_word += values.upper()
            else:
                new_word += values.lower()
        answer += [new_word]
    answer = " ".join(answer)

    return answer

print(solution("try hello world"))
