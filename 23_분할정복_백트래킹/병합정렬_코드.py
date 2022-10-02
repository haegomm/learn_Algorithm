# 병합 정렬 - 추가적으로 리스트를 만들고있기 때문에 메모리의 낭비가 조금 있다...?
def merge(left, right):
    merged_arr = []
    i, j = 0, 0  # 왼쪽, 오른쪽 리스트의 각각의 인덱스

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 왼쪽 리스트의 원소가 작거나 같으면 삽입
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[i])
            j += 1

    merged_arr.extend(left[i:])  # 뭐가 남아있는지 모르니깐 일단 넣어. i가 리스트 넘어가도...? 오류가 안난다고...? 왜....? 못들었....ㅠ 빈리스트를 반환한다고...?
    merged_arr.extend(right[j:])  # 남아 있는 애들 넣기. 큰 숫자들이 남아 있는거니깐?

    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:  # 더 이상 분할할 수 없는 경우(종료 조건)
        return arr

    # 1. 리스트를 분할하여 각각 정렬
    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    # 2. 정렬된 두 리스트를 병합
    return merge(left_arr, right_arr)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)