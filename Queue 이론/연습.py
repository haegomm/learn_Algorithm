from collections import deque

n = 3
queue = deque(range(1, n + 1))
print(queue[0])

queue.popleft()

print(queue[0])