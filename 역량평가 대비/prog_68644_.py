from itertools import combinations

def solution(numbers):
    answer = []
    length = 2

    for case in combinations(numbers, length):
        if sum(case) not in answer:
            answer.append(sum(case))

    answer.sort()

    return answer