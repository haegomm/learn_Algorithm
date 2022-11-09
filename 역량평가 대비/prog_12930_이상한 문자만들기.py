def solution(s):
    words = s.split(' ')
    answer = []

    for word in words:
<<<<<<< HEAD
        word = list(word)
        for i in range(0, len(word), 2):
            word[i] = word[i].upper()
        word = "".join(word)
        answer += [word]
=======
        new_word = ''
        for i, values in enumerate(word):
            if i % 2 == 0:
                new_word += values.upper()
            else:
                new_word += values.lower()
        answer += [new_word]
>>>>>>> 654183155016e75adb3533efd921f7300ae9b836
    answer = " ".join(answer)

    return answer

print(solution("try hello world"))
