# 1 ~ 12까지 8을 건너뛰고 출력 1
'''
이 프로그램은 비효율적
건너뛰는 판단을 하려면 비용이 많이 들기 때문
건너뛰어야 하는 값을 모르거나, 건너뛰어야 하는 값이 변화한다면 매번
if, continue 문을 사용해야합니다.
'''
for i in range(1, 12):
    if i == 8:
        continue
    
    print(f'{i}', end=" ")
    
print()