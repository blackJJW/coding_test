A, B = map(int, input().split(" "))
C = int(input())

total_m = B + C
plus_h = 0

if total_m > 59:
    plus_h = total_m // 60
    if A + plus_h > 23:
        print("%d %d" % ( (A + plus_h - 24), total_m % 60 ))
    else:
        print("%d %d" % ( (A + plus_h), total_m % 60 ))
else:
    print("%d %d" % ( A, total_m ))