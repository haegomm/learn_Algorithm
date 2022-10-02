import sys

sys.stdin = open('input.txt')


def partition(arr, left, right):
    pivot = arr[left]  # 가장 왼쪽 원소를 피벗으로 지정
    i, j = left, right  # 인덱스값 설정

    while i <= j:  # 값을 계속 찾고 계속 바꿔주기 위한  큰 반복문
        while i <= j and arr[i] <= pivot:  # 큰 값을 찾는거니깐 작은 값이고 i와 j가 역전되지 않았다면
            i += 1  # i 이동
        while i <= j and arr[j] >= pivot:  # 작은 값을 찾는거니깐 큰 값이고 i와 j가 역전되지 않았다면
            j -= 1  # j 이동
        if i < j:  # 위의 while문에서 큰 값과 작은 값을 찾아서 일단 멈춰서 if문으로 들어왔고,i의 위치가 j 보다 왼쪽이면
            arr[i], arr[j] = arr[j], arr[i]  # 위치값들을 바꿔준다
    arr[left], arr[j] = arr[j], arr[left]  # i와 j가 역전되면 while문 종료되고 정렬 끝났으니깐
                                           # 피벗과 j를 바꿔준다.
                                           # i는 큰 값의 시작이라 i랑 바꿔버리면 큰 값이 왼쪽으로 오게 됨
                                           # 그래서 j랑 바꿔주기!!
    return j  # j가 return 되면 middle = j


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)  # 리스트의 값들을 나눠보자(분할)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)


for t in range(1, int(input()) + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, n-1)  # 리스트와, l 시작값, r 시작값
    print(f'#{t}', numbers[n//2])

