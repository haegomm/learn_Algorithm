def f(n):
    if n == 0:
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1

def find_root(v):
    for i in range(1, V+1):
        if par[i] == 0:
            return i

def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])

def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)

E = int(input())
arr = list(map(int, input().split()))
V = E + 1

# V = int(input())
# arr = list(map(int, input().split()))
# E = V - 1

ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

par = [0] * (V+1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

root = find_root(V)
print(f())
# preorder(root)

