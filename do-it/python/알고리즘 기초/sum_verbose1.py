# a부터 b까지 정수의 합 구하기

print('a부터 b까지 정수의 합 ')

a = int(input('정수 a : '))
b = int(input('정수 b : '))

if a > b:
    a, b = b, a # a와 b를 오름차순으로 정렬
    
sum = 0

for i in range(a, b + 1):
    if i < b: # i가 b보다 작으면 합을 구하는 과정 출력
        print(f"{i} + ", end="")
        
    else: # i가 b보다 크거나 같으면 최종값 출력을 위해 i = 출력
        print(f"{i} = ", end="")
    sum += i # sum에 i를 더함
    
print(f"{sum}")