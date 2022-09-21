def selection_sort(arr):
    for i in range(len(arr)):  # 하나하나 다 봐야하니깐 len(arr)로 범위주기
        min_idx = i  # min_idx를 정렬되지 않은 부분의 맨 앞으로 초기화해주기

        for j in range(i + 1, len(arr)):  # '정렬 되지 않은 맨 앞 인덱스 + 1'부터 비교시작
            if arr[j] < arr[min_idx]:  # min_idx보다 작은 값을 찾으면
                min_idx = j  # 찾은 값으로 min_idx 바꿔주기

        arr[i], arr[min_idx] = (
            arr[min_idx],
            arr[i],
        )  # 정렬을 위한 i는 제일 작은 값을 찾기 전에 위치가 바뀌면 안됨.
        # 제일 작은 값을 앞으로 보내줘야하니깐
        # 작은 값을 찾는 for문이 종료되고 나서 위치바꿔주기.
        # 고로 자주하는 실수인 들여쓰기 주의!!


numbers = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
selection_sort(numbers)
print(numbers)


#
def seleciton_sort(i, n):
    if i == n - 1:  # 종료조건
        return  # 마지막 원소는 제일 큰 값이 남은거니깐 자동으로 제일 마지막 값이 되므로
        # 정렬할 필요가 없어짐
        # 따라서 재귀를 끝내줘야함

    min_idx = i  # min_idx를 정렬되지 않은 부분의 맨 앞으로 초기화해주기

    for j in range(i + 1, n):  # '정렬 되지 않은 맨 앞 인덱스 + 1'부터 비교시작
        if numbers[j] < numbers[min_idx]:  # min_idx보다 작은 값을 찾으면
            min_idx = j  # 찾은 값으로 min_idx 바꿔주기

    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    seleciton_sort(i + 1)  # 재귀 함수(나랑 똑같이 생긴 다른 함수) 호출


numbers = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
n = len(numbers)
seleciton_sort(0, n)  # 0번째 원소부터 정렬 시작
print(numbers)
