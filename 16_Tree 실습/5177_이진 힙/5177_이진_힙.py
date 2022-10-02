import sys
sys.stdin = open('input.txt')


def heap_push(k):
    heap.append(k)
    child = len(heap) - 1
    parent = child // 2

    while parent > 0 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    heap = [0]
    result = 0
    for k in numbers:
        heap_push(k)
    while n > 0:
        n = n // 2
        result += heap[n]

    # result = heap[n // 2] + heap[n // 2 - 1]
    print(heap)
    print(f'#{tc}', result)
