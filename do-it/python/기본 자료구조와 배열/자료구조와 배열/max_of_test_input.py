from max import max_of

print("배열의 최댓값을 구함")
print("End를 입력하면 종료")

number = 1
x = []

while True:
    s = input(f"x[{number}] 값을 입력 : ")
    if s == 'End':
        break
    
    x.append(int(s)) # 배열의 맨 끝에 추가
    number += 1
    
print(f"{number}개를 입력")
print(f"최댓값은 {max_of(x)}")
    