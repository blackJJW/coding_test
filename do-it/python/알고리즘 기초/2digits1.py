# 2자리 양수(10 ~ 99) 입력 받기

print('2자리 양수 입력 받기')

while True:
    no = int(input('값을 입력 : '))
    
    if no >= 10 and no <= 99:
        break
    
print(f"입력 받은 양수 : {no}")