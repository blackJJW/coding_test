# a부터 b까지 정수의 합 구하기
# sum_verbose1보다 효율이 좋음
print('a부터 b까지 정수의 합 ')

a = int(input('정수 a : '))
b = int(input('정수 b : '))

if a > b:
    a, b = b, a # a와 b를 오름차순으로 정렬
    
sum = 0

for i in range(a, b):
    print(f"{i} + ", end="")
    sum += i
        
print(f"{b} = ", end="")
sum += b
    
print(f"{sum}")