a, b = map(int, input().split())

x = [ 0 for _ in range(a) ]

for _ in range(b):
    c, d, e = map(int, input().split())
    for i in range(c - 1, d):
        x[i] = e
print(*x)