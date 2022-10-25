def solution(s):
    n = len(s)
    # m = n // 2
    #
    # if n % 2 == 1:
    #     answer = s[m]
    # else:
    #     answer = s[m-1:m+1]
    #

    answer = s[(n-1)//2: n//2+1]

    return answer


print(solution("qwer"))