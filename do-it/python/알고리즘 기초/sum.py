# a부터 b까지 정수의 합 구하기(for)

print('a부터 b까지 정수의 합 ')

a = int(input('정수 a : '))
b = int(input('정수 b : '))

if a > b:
    a, b = b, a # a와 b를 오름차순으로 정렬
    
sum = 0

for i in range(a, b + 1):
    sum += i
    
print(f"총 합 : {sum}")