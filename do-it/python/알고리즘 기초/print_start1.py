# *를 n개 출력하되 w개마다 줄바꿈 1

print('*를 출력')
n = int(input('몇 개 출력 : '))
w = int(input('몇 개마다 줄바꿈 :'))

for i in range(n): 
    print('*', end='')
    if i % w == w - 1:
        print()
        
if n % w:
    print()