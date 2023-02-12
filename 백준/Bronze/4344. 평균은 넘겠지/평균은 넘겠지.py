cnt = int(input())
lis = []
result = []
stu_result = []

for i in range(cnt):
    a = list(map(int, input().split(" ")))
    lis.append(a)
    
for i in range(len(lis)):
    sum = 0
    for j in range(len(lis[i]) - 1):
        sum += lis[i][j + 1]
    avg = (sum/lis[i][0])
    result.append(avg)

for i in range(len(result)):
    tmp = 0
    for j in range(len(lis[i]) - 1):
        if lis[i][j + 1] > result[i]:
            tmp += 1
        else:
            continue
    stu_result.append((tmp/lis[i][0]) * 100)
    
for i in stu_result:
    print(f'{i:.3f}%')
    