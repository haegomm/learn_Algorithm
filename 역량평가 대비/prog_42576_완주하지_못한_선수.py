def solution(participant, completion):
    d = {}
    for p in participant:
        if p in d:
            d[p] += 1  # d[p] = d[p] + 1
        else:
            d[p] = 1
    for c in completion:
        d[c] -= 1

    for k in d.items():
        if k[1] == 1:
            answer = k[0]
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))