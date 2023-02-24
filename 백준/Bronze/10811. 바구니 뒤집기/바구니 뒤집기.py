n, m = map(int, input().split())
a = [ x for x in range(1, n + 1) ]

for i in range(m):
    x, y = map(int, input().split())
    if x - 1 == 0:
        a[x-1:y] = a[y-1::-1]
    else:
        a[x-1:y] = a[y-1:x-2:-1]
print(*a)