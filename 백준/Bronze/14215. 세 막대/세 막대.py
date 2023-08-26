a, b, c = map(int, input().split())

tmp = max(a, b, c)
rest_tmp = (a + b + c) - tmp

if tmp < rest_tmp:
    print(a + b + c)
else:
    print(rest_tmp * 2 - 1)