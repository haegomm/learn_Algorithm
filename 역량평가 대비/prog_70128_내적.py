def solution(a, b):
    answer = 0
    n = len(a)
    for i in range(n):
        answer += (a[i] * b[i])

    return answer


# def solution(a, b):

#    return sum([x*y for x, y in zip(a,b)])