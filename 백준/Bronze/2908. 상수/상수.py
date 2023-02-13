a, b = map(int, input().split())

tmp_a = int(str(a)[::-1])
tmp_b = int(str(b)[::-1])

if tmp_a > tmp_b:
    print(tmp_a)
else:
    print(tmp_b)