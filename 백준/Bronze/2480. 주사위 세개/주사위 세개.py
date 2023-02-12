a, b, c = map(int, input().split(" "))

if a == b:
    if a == c:
        print(10000 + (1000 * a))
    else:
        print(1000 + (100 * a))
elif b == c:
    if a == c:
        print(10000 + (1000 * b))
    else:
        print(1000 + (100 * c))
elif a == c:
    if a == b:
        print(10000 + (1000 * c))
    else:
        print(1000 + (100 * a))
else:
    print(max(a, b, c) * 100)
        