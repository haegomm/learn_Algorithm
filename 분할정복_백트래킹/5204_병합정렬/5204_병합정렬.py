import sys

sys.stdin = open('input.txt')


def merge(left, right):
    global cnt                            # 횟수를 세주기 위한 변수를 받아온다
    merged_arr = []                       # 정렬한 값들을 담을 새 리스트 만들어주기
    i, j = 0, 0                           # 왼쪽, 오른쪽 리스트의 각각의 인덱스

    if left[-1] > right[-1]:              # 왼쪽 리스트 값이 오른쪽 리스트 값보다 크면
        cnt += 1                          # 횟수 +1

    while i < len(left) and j < len(right):  # i와 j는 각 리스트의 길이 만큼만 반복

        if left[i] <= right[j]:              # 만약에 왼쪽 i인덱스 값보다 오른쪽 j인덱스 값이 크면
            merged_arr.append(left[i])       # 오름차순이니깐 새로 만든 리스트에 왼쪽 값 넣어주고
            i += 1                           # i 옮기자
        else:                                # 오른쪽 j인덱스 값이 더 작다면
            merged_arr.append(right[j])      # 오른쪽[j]값 넣어주고
            j += 1                           # j 옮기자

    merged_arr.extend(left[i:])              # 정렬을 다하고도 남아있는 값이 있을 수 있으니깐 나머지 다 넣고
    merged_arr.extend(right[j:])             # 오른쪽도 마찬가지로 남아있는 값이 있을 수 있으니깐 나머지 다 넣기

    return merged_arr                        # 정렬한거 return 하기


def merge_sort(arr):
    if len(arr) <= 1:                      # 더 이상 분할할 수 없는 경우(종료 조건)
        return arr
                                           # 1. 리스트를 분할

    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle])    # 왼쪽 리스트
    right_arr = merge_sort(arr[middle:])   # 오른쪽 리스트

    return merge(left_arr, right_arr)      # 2. 분할 하였으니 병합하러~!


for t in range(1, int(input()) + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    sorted_numbers = merge_sort(numbers)

    print(f'#{t}', sorted_numbers[n//2], cnt)