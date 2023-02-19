n = int(input())
lst = map(int, input().split())

cnt = 0

for i in lst:
    error = 0
    if i > 1:
        for a in range(2, i):
            if i % a == 0:
                error += 1
        if error == 0:
            cnt += 1
print(cnt)
