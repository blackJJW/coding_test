# 1 부터 n까지 정수의 합 구하기(n값은 양수만 입력받음)

print('1부터 n까지의 정수의 합을 구한다.')

while True:
    n = int(input('n값을 입력 : '))
    
    if n > 0:
        break
    
sum = 0
i = 1

for i in range(1, n + 1):
    sum += i # sum에 1을 더함
    i += 1
    
print(f"합 : {sum}")