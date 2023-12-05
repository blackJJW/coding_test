import random
from max import max_of

print("난수 최댓값")

num = int(input('난수의 개수 입력 : '))
lo = int(input('난수의 최솟값 입력 : '))
hi = int(input('난수의 최댓값 입력 : '))

x = [None] * num  # 원소 수가 num인 리스트 생성

for i in range(num):
    x[i] = random.randint(lo, hi)
    
print(f'{x}')
print(f'최댓값 : {max_of(x)}')