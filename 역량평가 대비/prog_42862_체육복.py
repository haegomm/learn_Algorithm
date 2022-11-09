def solution(n, lost, reserve):
    no = len(lost)
    for r in reserve:
        if r in lost:
            lost.remove(r)
            no -= 1

        elif r - 1 in lost:
            lost.remove(r - 1)
            no -= 1

        else:
            if r + 1 in lost:
                lost.remove(r + 1)
                no -= 1

    answer = n - no

    return answer

print(solution(5, [3, 4], [4, 5]))