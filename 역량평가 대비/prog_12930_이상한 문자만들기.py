def solution(s):
    words = s.split(' ')
    answer = []

    for word in words:
        word = list(word)
        for i in range(0, len(word), 2):
            word[i] = word[i].upper()
        word = "".join(word)
        answer += [word]
    answer = " ".join(answer)

    return answer

print(solution("try hello world"))