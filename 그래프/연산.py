from collections import deque

cal = {
    0 : lambda x: x + 1,
    1 : lambda x: x - 1,
    2 : lambda x: x * 2,
    3 : lambda x: x - 10,
}

# lambda
# def asd(x):
#     return x + 1


def bfs(v, cnt):                                                   # bfs
    q = deque([(v, cnt)])                                          # 연산한 값이랑 연산횟수랑 같이 묶어서 큐에 넣어준다.
    check = set()                                                  # 중복된 값을 또 연산하지 않기 위한 set을 선언

    while q:                                                       # bfs 시작~!
        x, cnt = q.popleft()                                       # 꺼내오자~
        if x == m:                                                 # 연산한 값이 목표값이 된다면
            break                                                  # 그만~
        for i in range(4):                                         # +1 -1 *2 -10을 해야하니깐 4번 반복
            next_x = cal[i](x)                                     # 연산하기
            if 0 < next_x <= 1000000 and next_x not in check:      # 가지치기
                q.append((next_x, cnt + 1))                        # 연산한 값과 연산 한번 했으니 연산횟수 +1 해서 다시 큐에 넣어주기
                check.add(next_x)                                  # 중복된 값이 나오는지 아닌지를 확인하기 위해 연한한 값을 check에도 넣어주자~!

    return cnt                                                     # 끝~!


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    print(f'#{t} {bfs(n, 0)}')

"""
3
2 7
3 15
36 1007
"""
