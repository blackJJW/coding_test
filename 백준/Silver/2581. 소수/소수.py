a = int(input())
b = int(input())

lst = []
for num in range(a, b + 1):
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
                break
        if error == 0:
            lst.append(num)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))
    